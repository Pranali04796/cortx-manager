# CORTX-CSM: CORTX Management web and CLI interface.
# Copyright (c) 2020 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.

import os
from csm.common.payload import *
from csm.common.errors import CsmError, InvalidRequest
from csm.core.blogic import const
from cortx.utils.log import Log
from cortx.utils.conf_store.conf_store import Conf as conf_store
from csm.common.process import SimpleProcess
from cortx.utils.security.cipher import Cipher, CipherInvalidToken

class ClusterIdFetchError(InvalidRequest):
    pass

class Conf:
    ''' Represents conf file - singleton '''
    _payloads = {}

    @staticmethod
    def init():
        ''' Initializes data from conf file '''
        pass

    @staticmethod
    def load(index, doc, force=False):
        if not os.path.isfile('%s' %doc):
            raise CsmError(-1, 'File %s does not exist' %doc)
        if index in Conf._payloads.keys():
            if force == False:
                raise Exception('index %s is already loaded')
            Conf.save(index)
        Conf._payloads[index] = Payload(doc)

    @staticmethod
    def get(index, key, default_val=None):
        ''' Obtain value for the given key '''
        return Conf._payloads[index].get(key) \
            if default_val is None else default_val

    @staticmethod
    def set(index, key, val):
        ''' Sets the value into the conf for the given key '''
        Conf._payloads[index].set(key, val)

    @staticmethod
    def delete(index, key):
        '''Deletes an entry from the configuration according to its key.

        :param key: Key to be deleted
        :return: Deleted value
        '''
        return Conf._payloads[index].pop(key, None)

    @staticmethod
    def save(index=None):
        indexes = [x for x in Conf._payloads.keys()] if index is None else [index]
        for index in indexes:
            Conf._payloads[index].dump()


class ConfSection:
    """Represents sub-section of config file"""

    def __init__(self, from_dict: dict):
        """
        Initialize ConfSection by dictionary object

        :param dict from_dict: base dictionary to create object from its keys and values
        """
        for key, value in from_dict.items():
            if isinstance(value, dict):
                setattr(self, key, ConfSection(value))
            else:
                setattr(self, key, value)


class DebugConf:
    """
    Class which simplifies work with debug settings in debug mode:

    make easy check whether debug-mode is enabled and requested option is set
    to desired value
    """

    def __init__(self, debug_settings: ConfSection):
        """
        Initialize debug configuration instance by debug settings

        """
        self._debug_settings = debug_settings

    def __getattr__(self, attr):
        return getattr(self._debug_settings, attr)

    @property
    def http_enabled(self):
        """
        Validates if debug mode is enabled and HTTP is chosen
        """
        return self._debug_settings.enabled == 'true' and self._debug_settings.http_enabled == 'true'

class Security:

    @staticmethod
    def decrypt_conf():
        """
        THis Method Will Decrypt all the Passwords in Config and Will Load the Same in CSM.
        :return:
        """
        cluster_id = conf_store.get(const.CSM_GLOBAL_INDEX, const.CLUSTER_ID_KEY)
        Log.info(f"Cluster id: {cluster_id}")
        if not cluster_id:
            raise ClusterIdFetchError("Failed to get cluster id.")
        for each_key in const.DECRYPTION_KEYS:
            Log.info(f"Each key---->{each_key}")
            Log.info(f"const.DECRYPTION_KEYS[each_key]: {const.DECRYPTION_KEYS[each_key]}")
            cipher_key = Cipher.generate_key(cluster_id,
                                             const.DECRYPTION_KEYS[each_key])
            Log.info(f"Cipher key: {cipher_key}")
            encrypted_value = conf_store.get(const.CSM_GLOBAL_INDEX, each_key)
            Log.info(f"encrypted_value: {encrypted_value}")
            try:
                decrypted_value = Cipher.decrypt(cipher_key,
                                                 encrypted_value.encode("utf-8"))
                conf_store.set(const.CSM_GLOBAL_INDEX, each_key,
                        decrypted_value.decode("utf-8"))
                Log.info(f"Decrypted passwords saved {decrypted_value.decode('utf-8')}")
            except CipherInvalidToken as error:
                import traceback
                Log.exception(f"Decryption for {each_key} Failed. {error}")
                Log.exception(f"{traceback.format_exc()}")
