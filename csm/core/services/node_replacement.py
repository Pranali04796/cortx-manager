#!/usr/bin/env python3
"""
 ****************************************************************************
 Filename:          maintenance.py
 Description:       Services for maintenance

 Creation Date:     02/11/2020
 Author:            Ajay Paratmandali

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""

from eos.utils.log import Log
from csm.common.errors import CsmError, CSM_INVALID_REQUEST
from csm.common.services import ApplicationService
from csm.core.blogic import const
from eos.utils.data.access import Query, SortBy, SortOrder
from eos.utils.data.access.filters import Compare
from csm.core.data.models.node_replace import ReplaceNode, JobStatus


class ReplaceNodeService(ApplicationService):
    def __init__(self, maintanence, provisioner, db):
        """
        Instantiate Replace Node Service Class
        """
        super(ReplaceNodeService, self).__init__()
        self._maintenance = maintanence
        self._provisioner = provisioner
        self._replace_node = ReplaceNode
        self._storage = db(self._replace_node)

    async def _verify_node_status(self, resource_name):
        """
        Verify whether the requested Node is in Shutdown State or Not if Not Ask User to Shut-it Down First.
        :param resource_name: Node ID for Replacing :type Str
        :return:
        """
        try:
            node_status = await self._maintenance.get_status()
        except CsmError as e:
            Log.error(e)
            return CsmError(rc=CSM_INVALID_REQUEST,
                            desc=const.STATUS_CHECK_FALED)

        resources = node_status.get(const.NODE_STATUS)
        for each_resource in resources:
            if each_resource.get(const.NAME) == resource_name and each_resource.get(const.SHUTDOWN):
                break
        else:
            raise CsmError(rc=CSM_INVALID_REQUEST, desc=const.SHUTDOWN_NODE_FIRST)

    async def begin_process(self, resource_name):
        """
        Start the Node Replacement Process.
        "param: resource_name:  Node ID for Replacing. :type: Str
        """
        #Todo: Commenting Verification Since the BUG EOS-9734 is Already Open.
        # await self._verify_node_status(resource_name)
        # Verify if any Process for Node Replacement is not Running.
        Log.debug("Verifying for Any Running Job")
        if await self.is_job_running():
            raise CsmError(rc=CSM_INVALID_REQUEST,
                           desc=const.NODE_REPLACEMENT_ALREADY_RUNNING)
        # Call Prvisioner API and Start Node Replacement.
        Log.debug("Calling Provisioner API.")
        try:
            job_id = await self._provisioner.start_node_replacement(resource_name)
        except Exception as e:
            #todo: Capture the Error Received From Provisioner And Add Appropriate Exception Classes.
            raise CsmError(rc=CSM_INVALID_REQUEST,
                            desc=f"{e}")
        # Save Received Process ID in Consul.
        model = self._replace_node.generate_new(job_id, resource_name)
        await self._storage.store(model)
        return {"msg": const.NODE_REPLACEMENT_STARTED.format(resource_name=resource_name)}

    async def is_job_running(self):
        """
        Check and Returns True for Running Job else False
        :return: True/False :Boolean
        """
        sort_by = SortBy(ReplaceNode.created_time, SortOrder.DESC)
        query = Query().order_by(sort_by.field, sort_by.order)
        data = await self._storage.get(query)
        if data and data[0].status == JobStatus.Is_Running:
            return True
        return False