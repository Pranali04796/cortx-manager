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

# Csm Setup
CSM_PATH = "/opt/seagate/cortx/csm"
CORTXCLI_PATH = "/opt/seagate/cortx/cli"
CSM_PIDFILE_PATH = "/var/run/csm"
CSM_LOG_PATH = "/var/log/seagate/csm/"
CSM_CLEANUP_LOG_FILE = "csm_cleanup"
CSM_S3_SANITY_LOG_FILE = "csm_s3_sanity"
CSM_SOURCE_CONF_PATH = "{}/conf/etc/csm/".format(CSM_PATH)
CORTXCLI_SOURCE_CONF_PATH = "{}/conf/etc/cli".format(CORTXCLI_PATH)
ETC_PATH = "/etc"
CSM_CONF_PATH = ETC_PATH + "/csm"
CORTXCLI_CONF_PATH = ETC_PATH + "/cli"
CSM_SOURCE_CONF = "{}/conf/etc/csm/csm.conf".format(CSM_PATH)
CSM_SOURCE_CONF_URL = f"yaml://{CSM_SOURCE_CONF}"
CSM_SETUP_LOG_DIR = "/tmp"
CSM_CONF_FILE_NAME = 'csm.conf'
CORTXCLI_CONF_FILE_NAME = 'cortxcli.conf'
CORTXCLI_CONF_FILE_URL = (f'yaml://{CORTXCLI_SOURCE_CONF_PATH}/'
                          f'{CORTXCLI_CONF_FILE_NAME}')
DB_CONF_FILE_NAME = 'database.yaml'
DB_SOURCE_CONF_FILE_URL = f'yaml://{CSM_PATH}/conf/etc/csm/{DB_CONF_FILE_NAME}'
PLUGIN_DIR = 'cortx'
WEB_DEFAULT_PORT = 28100 # currently being used by USL only
PROVISIONER_LOG_FILE_PATH = "/var/log/seagate"
# Access log of aiohttp
# format
MARSHMALLOW_EXCLUDE = "EXCLUDE"
CSM_SETUP_PASS = ":PASS"

# Commands
CSM_SETUP_CMD = 'csm_setup'
INTERACTIVE_SHELL_HEADER = """
**********************************\n
CORTX Interactive Shell
Type -h or --help for help.\n
***********************************
"""

CLI_PROMPT = "cortxcli$ "

EMAIL_CONFIGURATION = 'email'
ALERTS_COMMAND = 'alerts'
BASE_DIR = '/opt/seagate/cortx'
CSM_INSTALL_BASE_DIR = BASE_DIR + '/csm'
CSM_SCHEMA_BASE_DIR = CSM_INSTALL_BASE_DIR + '/schema'
COMMAND_DIRECTORY = "{}/cli/schema".format(CORTXCLI_PATH)
SUB_COMMANDS_PERMISSIONS = "permissions_tag"
NO_AUTH_COMMANDS = ["support_bundle", "bundle_generate", "csm_bundle_generate",
                    "-h", "--help", "system"]
EXCLUDED_COMMANDS = ['csm_setup']
HIDDEN_COMMANDS = ["bundle_generate", "csm_bundle_generate",]
RMQ_CLUSTER_STATUS_CMD = 'rabbitmqctl cluster_status'
RUNNING_NODES = 'running_nodes'
RUNNING_NODES_START_TEXT = 'Running Nodes'
RUNNING_NODES_STOP_TEXT = 'Versions'

# CSM Agent Port
CSM_AGENT_HOST = "localhost"
CSM_AGENT_HOST_PARAM_NAME = "csm_agent_host"
ADDRESS_PARAM = "Address"
CSM_AGENT_PORT = 8101
CSM_AGENT_BASE_URL = "http://"
TIMEOUT = 60

# Initalization
HA_INIT = '/var/csm/ha_initialized'

#HA Command
HCTL_NODE = 'hctl node --username {user} --password {pwd} {command}'
CORTXHA_CLUSTER = 'cortxha cluster {command}'
HCTL_ERR_MSG = "Failed to execute command.\nPlease check logs for detailed error."
HCTL_NOT_INSTALLED = "System is not provisioned correctly."
INVALID_RESOURCE = "Invalid resource selected."
RESOURCE_ALREADY_SHUTDOWN = "Resource selected is already in shutdown mode."
# File names
SUMMARY_FILE = 'summary.txt'

# Cluster states
STATE_UP = 'up'
STATE_DOWN = 'down'
STATE_DEGRADED = 'degraded'

# ERROR CODES
SUPPORT_BUNDLE_NOT_FOUND = 1000
OS_PERMISSION_DENIED = 2000

# File Collector
BUNDLE_FILE = 'files.tgz'

# Security
CERT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z"

# Poll check internal
RESPONSE_CHECK_INTERVAL = 1

# Index
CSM_GLOBAL_INDEX = 'CSM'
INVENTORY_INDEX = 'INVENTORY'
COMPONENTS_INDEX = 'COMPONENTS'
DATABASE_INDEX = 'DATABASE'
CONSUMER_INDEX = 'CONSUMER'
TEST_INDEX = 'TEST'
CORTXCLI_GLOBAL_INDEX = 'CORTXCLI'
USL_GLOBAL_INDEX = 'USL'

# Cluster Inventory Related
INVENTORY_FILE = '/etc/csm/cluster.conf'
KEY_COMPONENTS = 'sw_components'
ADMIN_USER = 'admin_user'
KEY_NODES = 'nodes'
TYPE_CMU = 'CMU'
TYPE_SSU = 'SSU'
TYPE_S3_SERVER = 'S3_SERVER'

# Config
CORTX = 'cortx'
TMP_CSM = '/tmp/csm'
CSM_ETC_DIR = '/etc/csm'
TMP_CSM = '/tmp/csm'
CSM_CONF = '/etc/csm/csm.conf'
USL_CONF = '/etc/csm/usl.conf'
CORTXCLI_CONF = '/etc/cli/cortxcli.conf'
CORTXCLI_SECTION = 'CORTXCLI'
CSM_CLUSTER_CONF = '/etc/csm/cluster.conf'
CSM_TMP_FILE_CACHE_DIR = '/tmp/csm/file_cache/transfer'
COMPONENTS_CONF = '/etc/csm/components.yaml'
DATABASE_CONF = '/etc/csm/database.yaml'
DATABASE_CONF_URL = f"yaml://{DATABASE_CONF}"
DATABASE_CLI_CONF = '/etc/cli/database_cli.yaml'
CSM_AGENT_SERVICE = "csm_agent.service"
CSM_AGENT_SERVICE_FILE_PATH = f"/etc/systemd/system/{CSM_AGENT_SERVICE}"
CSM_WEB_SERVICE = "csm_web.service"
CSM_WEB_SERVICE_FILE_PATH = f"/etc/systemd/system/{CSM_WEB_SERVICE}"
CSM_WEB_ENV_FILE_PATH = f"{BASE_DIR}/csm/web/.env"
CSM_WEB_DIST_ENV_FILE_PATH = f"{BASE_DIR}/csm/web/web-dist/.env"
CSM_FILES = [CSM_AGENT_SERVICE_FILE_PATH, CSM_WEB_SERVICE_FILE_PATH]
SUPPORT_BUNDLE_ROOT = 'SUPPORT_BUNDLE_ROOT'
DEFAULT_SUPPORT_BUNDLE_ROOT = BASE_DIR + '/bundle'
SSH_TIMEOUT = 'SSH_TIMEOUT'
SSH_KEY = 'id_rsa_prvsnr'
DEFAULT_SSH_TIMEOUT = 10
USER = 'user'
DEFAULT_USER = 'admin'
CSM_SUPER_USER_ROLE = 'admin'
CSM_MANAGE_ROLE = 'manage'
CSM_MONITOR_ROLE = 'monitor'
CSM_S3_ACCOUNT_ROLE = 's3'
CSM_USER_ROLES = [CSM_SUPER_USER_ROLE, CSM_MANAGE_ROLE, CSM_MONITOR_ROLE]
CSM_USER_INTERFACES = ['cli', 'web', 'api']
CSM_CONF_URL = f"yaml://{CSM_CONF_PATH}/{CSM_CONF_FILE_NAME}"
DATABASE_CONF_URL = f"yaml://{DATABASE_CONF}"
CSM_MAX_USERS_ALLOWED = "CSM_USERS>max_users_allowed"

# cron dir
CRON_DIR = "/etc/cron.daily"
SOURCE_CRON_PATH = "{0}/conf{1}/es_logrotate.cron".format(CSM_PATH, CRON_DIR)
DEST_CRON_PATH = "{}/es_logrotate.cron".format(CRON_DIR)

# Non root user
NON_ROOT_USER = 'csm'
NON_ROOT_USER_KEY = 'CSM>username'
CSM = 'CSM'
CSM_USER_HOME='/opt/seagate/cortx/csm/home/'
HA_CLIENT_GROUP = 'haclient'
SSH_DIR='.ssh'
SSH_PRIVATE_KEY='{}/id_rsa'.format(SSH_DIR)
SSH_PUBLIC_KEY='{}/id_rsa.pub'.format(SSH_DIR)
SSH_AUTHORIZED_KEY='{}/authorized_keys'.format(SSH_DIR)
SSH_CONFIG='{}/config'.format(SSH_DIR)
PRIMARY_ROLE='primary'
CONFIG_URL = 'config_url'

# CSM Alert Related
CSM_ALERT_CMD = 'cmd'
GOOD_ALERT = ['insertion', 'fault_resolved', 'resolved', 'threshold_breached:up']
BAD_ALERT = ['missing', 'fault', 'threshold_breached:low', 'threshold_breached:high']
SW = 'SW'
HW = 'HW'
ALERT_TYPE = 'type'
HEALTH_ALERT_TYPE = 'alert_type'
ALERT_UUID = 'alert_uuid'
ALERT_STATE = 'state'
ALERT_ENCLOSURE_ID = 'enclosure_id'
ALERT_MODULE_NAME = 'module_name'
ALERT_RESOLVED = 'resolved'
ALERT_ACKNOWLEDGED = 'acknowledged'
ALERT_SEVERITY = 'severity'
ALERT_RESOURCE_TYPE = 'resource_type'
ALERT_MODULE_TYPE = 'module_type'
ALERT_UPDATED_TIME = 'updated_time'
ALERT_CREATED_TIME = 'created_time'
ALERT_INT_DEFAULT = -1
ALERT_TRUE = 1
ALERT_FALSE = 0
ALERT_SENSOR_TYPE = 'sensor_response_type'
ALERT_MESSAGE = 'message'
ALERT_COMMENT = 'comment'
ALERT_SENSOR_INFO = 'sensor_info'
ALERT_MAX_COMMENT_LENGTH = 255
ALERT_SORTABLE_FIELDS = ['created_time', 'updated_time', 'severity', 'resolved',
                         'acknowledged']
ALERT_EVENT_DETAILS = 'event_details'
ALERT_EXTENDED_INFO = 'extended_info'
ALERT_EVENTS = 'events'
ALERT_NAME = 'name'
ALERT_COMPONENT_ID = 'component_id'
ALERT_EVENT_REASON = 'event_reason'
ALERT_EVENT_RECOMMENDATION = 'event_recommendation'
ALERT_HEALTH_REASON = 'health_reason'
ALERT_HEALTH_RECOMMENDATION = 'health_recommendation'
ALERT_CURRENT = 'current'
ALERT_VOLTAGE = 'voltage'
ALERT_TEMPERATURE = 'temperature'
ALERT_SENSOR_NAME = 'sensor_name'
ALERT_CONTAINER = 'container'
ALERT_DURABLE_ID = 'durable_id'
ALERT_LOGICAL_VOLUME = 'logical_volume'
ALERT_VOLUME = 'volume'
ALERT_SIDEPLANE = 'sideplane'
ALERT_FAN = 'fan'
ALERT_HEALTH = 'health'
ALERT_INFO = 'info'
ALERT_SITE_ID = 'site_id'
ALERT_CLUSTER_ID = 'cluster_id'
ALERT_RACK_ID = 'rack_id'
ALERT_NODE_ID = 'node_id'
ALERT_RESOURCE_ID = 'resource_id'
ALERT_EVENT_TIME = 'event_time'
TIME = 'time'
IEM_ALERT = 'iem_alert'
DESCRIPTION = 'description'
INFORMATIONAL = 'informational'
COMPONENT_ID = 'component'
SOURCE_ID = 'source'
MODULE_ID = 'module'
EVENT_ID = 'event'
IEM = 'iem'
SPECIFIC_INFO = 'specific_info'
SUPPORT_MESSAGE = 'support_message'
CRITICAL='critical'
ERROR='error'
WARNING='warning'

# Health
OK_HEALTH = 'OK'
NA_HEALTH = 'NA'
TOTAL = 'total'
GOOD_HEALTH = 'good'
HEALTH_SUMMARY = 'health_summary'
RESOURCE_KEY = 'resource_key'
HOST = 'host'
PORT = 'port'
UNAME = 'username'
PASS = 'password'
RETRY_COUNT = 'retry_count'
DURABLE = 'durable'
SLEEP_TIME = 'sleep_time'
ENCLOSURE = 'enclosure'
NODE = 'node'
HEADER = 'sspl_ll_msg_header'
UUID = 'uuid'
ACT_REQ_TYPE = 'actuator_request_type'
STORAGE_ENCL = 'storage_enclosure'
ENCL_REQ = 'enclosure_request'
ENCL = 'ENCL:'
NODE_CONTROLLER = 'node_controller'
NODE_REQ = 'node_request'
NODE_HW = 'NDHW:'
KEY = 'key'
HEALTH_FIELD ='health_field'
RES_ID_FIELD = 'res_id_field'
MAPPING_KEY = 'mapping_key'
RESOURCE_LIST = 'resource_list'
DURABLE_ID = 'durable_id'
NODE_RESPONSE = 'node_response'
FETCH_TIME = 'fetch_time'
HOST_ID = 'host_id'
CREATED_TIME = 'created_time'
FAULT_HEALTH = 'Fault'
RESPONSE_FORMAT_TREE = 'tree'
RESPONSE_FORMAT_TABLE = 'flattened'
ARG_RESOURCE = 'resource'
ARG_RESOURCE_ID = 'resource_id'
ARG_DEPTH = 'depth'
HEALTH_DEFAULT_DEPTH = 1
ARG_RESPONSE_FORMAT = 'response_format'
ARG_OFFSET = 'offset'
HEALTH_DEFAULT_OFFSET = 1
ARG_LIMIT = 'limit'
HEALTH_DEFAULT_LIMIT = 0
FETCH_RESOURCE_HEALTH_REQ = 'fetch_resource_health'
FETCH_RESOURCE_HEALTH_BY_ID_REQ = 'fetch_resource_health_by_id'
STATUS_LITERAL = 'status'
OUTPUT_LITERAL = 'output'
ERROR_LITERAL = 'error'
STATUS_SUCCEEDED = 'Succeeded'
STATUS_FAILED = 'Failed'
STATUS_PARTIAL = 'Partial'
HEALTH_FETCH_ERR_MSG = 'Error fetching health from ha.'

# CSM Schema Path
ALERT_MAPPING_TABLE = '{}/schema/alert_mapping_table.json'.format(CSM_PATH)
HEALTH_MAPPING_TABLE = '{}/schema/csm_health_schema.json'.format(CSM_PATH)
CSM_SETUP_FILE = '{}/schema/csm_setup.json'.format(CSM_PATH)
CLI_SETUP_FILE = '{}/cli_setup.json'.format(COMMAND_DIRECTORY)

# Support Bundle
SSH_USER_NAME = 'root'
COMMANDS_FILE = "{}/schema/commands.yaml".format(CORTXCLI_PATH)
SUPPORT_BUNDLE_TAG = "support_bundle;"
SUPPORT_BUNDLE = 'SUPPORT_BUNDLE'
SOS_COMP = 'os'
SB_COMPONENTS = "components"
SB_COMMENT = "comment"
SB_NODE_NAME = "node_name"
SB_BUNDLE_ID = "bundle_id"
SB_BUNDLE_PATH = "bundle_path"
SB_SYMLINK_PATH = "symlink_path"
ROOT_PRIVILEGES_MSG = "Command requires root privileges"
PERMISSION_ERROR_MSG = "Failed to cleanup {path} due to insufficient permissions"

# CSM Stats Related
AGGREGATION_RULE = '{}/schema/stats_aggregation_rule.json'.format(CSM_PATH)

# CSM Roles Related
ROLES_MANAGEMENT = '{}/schema/roles.json'.format(CSM_PATH)
CLI_DEFAULTS_ROLES = '{}/cli/schema/cli_default_roles.json'.format(CORTXCLI_PATH)
PERMISSIONS = "permissions"
LYVE_PILOT = "lyve_pilot"

# S3
S3_HOST = 'S3>host'
S3_IAM_PORT = 'S3>iam_port'
S3_PORT = 'S3>s3_port'
S3_MAX_RETRIES_NUM = 'S3>max_retries_num'
S3_LDAP_LOGIN = 'S3>ldap_login'
S3_LDAP_PASSWORD = 'S3>ldap_password'

S3_CREATE_ACCOUNT_RESP_ACCOUNT_PATH = (
    'CreateAccountResponse', 'CreateAccountResult', 'Account')
S3_CREATE_ACCOUNT_LOGIN_PROFILE_RESP_PROFILE_PATH = (
    'CreateAccountLoginProfileResponse', 'CreateAccountLoginProfileResult', 'LoginProfile')
S3_LIST_ACCOUNTS_RESP_ACCOUNTS_PATH = (
     'ListAccountsResponse', 'ListAccountsResult', 'Accounts')
S3_LIST_ACCOUNTS_RESP_ISTRUNCATED_PATH = (
    'ListAccountsResponse', 'ListAccountsResult', 'IsTruncated')
S3_LIST_ACCOUNTS_RESP_MARKER_PATH = (
    'ListAccountsResponse', 'ListAccountsResult', 'Marker')
S3_RESET_ACCOUNT_ACCESS_KEY_RESP_ACCOUNT_PATH = (
    'ResetAccountAccessKeyResponse', 'ResetAccountAccessKeyResult', 'Account')
S3_CREATE_USER_RESP_USER_PATH = (
    'CreateUserResponse', 'CreateUserResult', 'User')
S3_LIST_USERS_RESP_ISTRUNCATED_PATH = (
    'ListUsersResponse', 'ListUsersResult', 'IsTruncated')
S3_LIST_USERS_RESP_MARKER_PATH = (
    'ListUsersResponse', 'ListUsersResult', 'Marker')
S3_CREATE_ACCESS_KEY_RESP_KEY_PATH = (
    'CreateAccessKeyResponse', 'CreateAccessKeyResult', 'AccessKey')
S3_GET_ACCESS_KEY_LAST_RESP_KEY_PATH = (
    'GetAccessKeyLastUsedResponse', 'GetAccessKeyLastUsedResult', 'AccessKeyLastUsed')
S3_LIST_ACCESS_KEYS_RESP_KEYS_PATH = (
    'ListAccessKeysResponse', 'ListAccessKeysResult', 'AccessKeyMetadata')
S3_LIST_ACCESS_KEYS_RESP_ISTRUNCATED_PATH = (
    'ListAccessKeysResponse', 'ListAccessKeysResult', 'IsTruncated')
S3_LIST_ACCESS_KEYS_RESP_MARKER_PATH = (
    'ListAccessKeysResponse', 'ListAccessKeysResult', 'Marker')
S3_GET_TMP_CREDS_RESP_CREDS_PATH = (
    'GetTempAuthCredentialsResponse', 'GetTempAuthCredentialsResult', 'AccessKey')


S3_IAM_CMD_CREATE_ACCESS_KEY = 'CreateAccessKey'
S3_IAM_CMD_UPDATE_ACCESS_KEY = 'UpdateAccessKey'
S3_ACCESS_KEY_STATUSES = ['Active', 'Inactive']
S3_IAM_CMD_GET_ACCESS_KEY_LAST_USED = 'GetAccessKeyLastUsed'  # not supported by the S3 server yet
S3_IAM_CMD_LIST_ACCESS_KEYS = 'ListAccessKeys'
S3_PARAM_USER_NAME = 'UserName'
S3_PARAM_MARKER = 'Marker'
S3_PARAM_MAX_ITEMS = 'MaxItems'
S3_IAM_CMD_DELETE_ACCESS_KEY = 'DeleteAccessKey'
USER_NAME = 'user_name'
S3_ACCESS_KEYS = 'access_keys'
S3_ACCESS_KEY_ID = 'access_key_id'
ROOT = 'root'

# S3/Boto3
S3_DEFAULT_REGION = 'us-west2'
S3_RESOURCE_NAME_IAM = 'iam'
S3_RESOURCE_NAME_S3 = 's3'
S3_DEFAULT_RETRIES_MODE = 'standard'
S3_DEFAULT_REQUEST_HEADERS = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'text/plain',
}
S3_RESP_LIST_ITEM = 'member'

# UDS/USL
UDS_SERVER_DEFAULT_BASE_URL = 'http://localhost:5000'
UDS_CERTIFICATES_PATH = '/var/csm/tls'
UDS_NATIVE_PRIVATE_KEY_FILENAME = 'native.key'
UDS_NATIVE_CERTIFICATE_FILENAME = 'native.crt'
UDS_DOMAIN_PRIVATE_KEY_FILENAME = 'domain.key'
UDS_DOMAIN_CERTIFICATE_FILENAME = 'domain.crt'

# USL S3 configuration (CES2020 only!)
USL_S3_CONF = '/etc/uds/uds_s3.toml'
# IAM User Related
PASSWORD_SPECIAL_CHARACTER = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                              "_", "+", "-", "=", "[", "]", "{", "}", "|", "'"]

# CSM Users
CSM_USER_NAME_MIN_LEN = 3
CSM_USER_NAME_MAX_LEN = 64
CSM_USER_SORTABLE_FIELDS = [
    'user_id', 'username', 'email', 'user_type', 'role', 'created_time', 'updated_time']
CSM_USER_DEFAULT_TIMEOUT = 0
CSM_USER_DEFAULT_LANGUAGE = 'English'
CSM_USER_DEFAULT_TEMPERATURE = 'celcius'
CSM_USER_CURRENT_PASSWORD = 'current_password'
CSM_USER_NAME = 'username'
# CONSTANT
STRING_MAX_VALUE = 250
PATH_PREFIX_MAX_VALUE = 512
PORT_MIN_VALUE = 0
PORT_MAX_VALUE = 65536

SOFTWARE_UPDATE_ID = 'software_update'
FIRMWARE_UPDATE_ID = 'firmware_update'
REPLACE_NODE_ID = 'replace_node'
# Email configuration
CSM_SMTP_SEND_TIMEOUT_SEC = 30
CSM_SMTP_RECONNECT_ATTEMPTS = 2
CSM_ALERT_EMAIL_NOTIFICATION_TEMPLATE_REL = '{}/templates/alert_notification_email.html'.format(
    CSM_PATH)
CSM_ALERT_EMAIL_NOTIFICATION_SUBJECT = 'Alert notification'
CSM_ALERT_NOTIFICATION_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
CSM_SMTP_TEST_EMAIL_ATTEMPTS = 1
CSM_SMTP_TEST_EMAIL_TIMEOUT = 15
CSM_SMTP_TEST_EMAIL_SUBJECT = 'CORTX: test email'
CSM_SMTP_TEST_EMAIL_TEMPLATE_REL = '{}/templates/smtp_server_test_email.html'.format(
    CSM_PATH)

# Appliance name config
APPLIANCE_NAME = 'appliance_name'
DEFAULT_APPLIANCE_NAME = 'local'

# NTP server config
DATE_TIME_SETTING = 'date_time_settings'
NTP = 'ntp'
NTP_SERVER_ADDRESS = 'ntp_server_address'
NTP_TIMEZONE_OFFSET = 'ntp_timezone_offset'

# Audit Log
CSM_AUDIT_LOG_SCHEMA = '{}/schema/csm_audit_log.json'.format(CSM_PATH)
AUDIT_LOG = "/tmp/auditlogs/"
MAX_RESULT_WINDOW = 10000
SORTABLE_FIELDS = "sortable_fields"

# Syslog constants
LOG_LEVEL = "INFO"
USL_POLLING_LOG = "usl_polling_log"

# Set network config
NETWORK_CONFIG = 'NETWORK_CONFIG'
MANAGEMENT_NETWORK = 'management_network_settings'
DATA_NETWORK = 'data_network_settings'
DNS_NETWORK = 'dns_network_settings'
IPV4 = 'ipv4'
NODES = 'nodes'
IP_ADDRESS = 'ip_address'
GATEWAY = 'gateway'
NETMASK = 'netmask'
HOSTNAME = 'hostname'
NAME = 'name'
SUMMARY = 'is_summary'
DNS_SERVER = 'dns_servers'
SEARCH_DOMAIN = 'search_domain'
VIP_NODE = 'VIP'
PRIMARY_NODE = 'Node 0'
SECONDARY_NODE = 'Node 1'
SYSTEM_CONFIG = 'system_config'
IS_DHCP = 'is_dhcp'
ROAMING_IP = "roaming_ip"
PRIVATE_IP = "private_ip"
LOCALHOST = "localhost"
NETWORK = "network"
DATA = "data"
PUBLIC_FQDN = "public_fqdn"
PRIVATE_FQDN = "private_fqdn"
MANAGEMENT = "management"
VIRTUAL_HOST = "virtual_host"
PUBLIC_DATA_DOMAIN_NAME = "node_public_data_domain_name"

# Services
AUDIT_LOG_SERVICE = "audit_log"
SYSTEM_CONFIG_SERVICE = "system_config_service"
PRODUCT_VERSION_SERVICE = "product_version_service"
CSM_USER_SERVICE = "csm_user_service"
S3_ACCOUNT_SERVICE = "s3_account_service"
S3_IAM_USERS_SERVICE = "s3_iam_users_service"
S3_BUCKET_SERVICE = "s3_bucket_service"
S3_ACCESS_KEYS_SERVICE = 's3_access_keys_service'
S3_SERVER_INFO_SERVICE = 's3_server_info_service'
APPLIANCE_INFO_SERVICE = "appliance_info_service"
UNSUPPORTED_FEATURES_SERVICE = "unsupported_features_service"
SYSTEM_STATUS_SERVICE = "system_status_service"

# System Status flight
SYSTEM_STATUS_CONSUL = 'consul'
SYSTEM_STATUS_ELASTICSEARCH = 'es'
SYSTEM_STATUS_SUCCESS = 'success'

# Rsyslog
RSYSLOG_DIR = "/etc/rsyslog.d"
SOURCE_RSYSLOG_PATH = "{0}/conf{1}/0-csm_logs.conf".format(CSM_PATH, RSYSLOG_DIR)
CLI_SOURCE_RSYSLOG_PATH = "{0}/conf{1}/0-cortxcli_logs.conf".format(CORTXCLI_PATH, RSYSLOG_DIR)
RSYSLOG_PATH = "{}/0-csm_logs.conf".format(RSYSLOG_DIR)
CLI_RSYSLOG_PATH = "{}/0-cortxcli_logs.conf".format(RSYSLOG_DIR)
CLI_SOURCE_SUPPORT_BUNDLE_CONF = "{0}/conf{1}/0-support_bundle.conf".format(CORTXCLI_PATH, RSYSLOG_DIR)
SUPPORT_BUNDLE_CONF = "{}/0-support_bundle.conf".format(RSYSLOG_DIR)

#cron dir
CRON_DIR="/etc/cron.daily"
SOURCE_CRON_PATH="{0}/conf{1}/es_logrotate.cron".format(CSM_PATH, CRON_DIR)
DEST_CRON_PATH="{}/es_logrotate.cron".format(CRON_DIR)

#logrotate
LOGROTATE_DIR = "/etc/logrotate.d"
LOGROTATE_DIR_DEST = "/etc/logrotate.d"

# https status code
STATUS_CREATED = 201
STATUS_CONFLICT = 409

SOURCE_LOGROTATE_PATH = "{0}/conf{1}/csm/csm_agent_log.conf".format(CSM_PATH, LOGROTATE_DIR)
LOGROTATE_PATH = "{}/".format(LOGROTATE_DIR)
CSM_LOGROTATE_DEST = "{0}/csm_agent_log.conf".format(LOGROTATE_DIR_DEST)

# Service instance literal constant
FW_UPDATE_SERVICE = "fw_update_service"
HOTFIX_UPDATE_SERVICE = "hotfix_update_service"
SECURITY_SERVICE = "security_service"
STORAGE_CAPACITY_SERVICE = "storage_capacity_service"
USL_SERVICE = "usl_service"
MAINTENANCE_SERVICE = "maintenance"
REPLACE_NODE_SERVICE = "replace_node"

# Plugins literal constansts
ALERT_PLUGIN = "alert"
HEALTH_PLUGIN = "health"
S3_PLUGIN = "s3"
PROVISIONER_PLUGIN = "provisioner"
PLUGIN_REQUEST = "request"

# REST METHODS
POST = "POST"
GET = "GET"
PUT = "PUT"
PATCH = "PATCH"
DELETE = "DELETE"

# Capacity api related constants
UNIT_LIST = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
DEFAULT_CAPACITY_UNIT = 'BYTES'
DEFAULT_ROUNDOFF_VALUE = 2
UNIT = 'unit'
ROUNDOFF_VALUE = 'roundoff'
FILESYSTEM_STAT_CMD = 'hctl status --json'
TOTAL_SPACE = 'fs_total_disk'
FREE_SPACE = 'fs_free_disk'
SIZE = 'size'
USED = 'used'
AVAILABLE = 'avail'
USAGE_PERCENTAGE = 'usage_percentage'

# Keys for  Description
DECRYPTION_KEYS = {
    "S3>ldap_password": "S3>password_decryption_key",
    "CSM>password": "CSM>password_decryption_key"
}
CLUSTER_ID_KEY = "PROVISIONER>cluster_id"
SERVER_NODE = "server_node"
ENCLOSURE_ID = "enclosure_id"
SOFTWARE = "software"

#Third party packages information
python_pkgs_req_path = CSM_INSTALL_BASE_DIR + "/conf/requirment.txt"
dependent_rpms = ["elasticsearch-oss-7.10", "consul-1.9", "opendistroforelasticsearch-kibana-1.12", "cortx-csm_web"]

# Provisioner status
PROVISIONER_CONFIG_TYPES = ['network', 'firmware', 'hotfix']

# Provisioner Plugin constant
NODE_LIST_KEY='cluster:node_list'
GRAINS_GET = 'grains.get'
PILLAR_GET = 'pillar.get'
S3 = 'S3'
RMQ = 'rmq'
USERNAME = "username"
PASSWORD = 'password'
SECRET = 'secret'
IAM_ADMIN = 'iam_admin'
OPENLDAP = 'openldap'
SSPL = 'sspl:LOGGINGPROCESSOR'
LDAP_LOGIN = 'ldap_login'
LDAP_PASSWORD = 'ldap_password'
CLUSTER_ID = 'cluster_id'
PROVISIONER = 'PROVISIONER'
RET='ret'
DEBUG='debug'
NA='NA'
GET_NODE_ID='get_node_id'
NODE_TYPE="node_type"
SGIAM = "sgiam"

#Deployment Mode
DEPLOYMENT = 'DEPLOYMENT'
MODE = 'mode'
DEV = 'dev'
VM = 'VM'
VIRTUAL = 'virtual'
ENV_TYPE = 'env_type'

# System config list
SYSCONFIG_TYPE = ['management_network_settings', 'data_network_settings',
                  'dns_network_settings', 'date_time_settings', 'notifications']
#Maintenance
STATE_CHANGE = "Successfully put {node} on {state} state"
ACTION = "action"
NODE_STATUS = "node_status"
STANDBY = "standby"
SHUTDOWN = "shutdown"
START = "start"
STOP = "stop"
ONLINE = "online"
RESOURCE_NAME = "resource_name"
REPLACE_NODE = "replace_node"
REPLACE_NODE_STATUS = "replace_node_status"
NODE_STATUS = "node_status"
INVALID_PASSWORD = f"Invalid {PASSWORD}"
STATUS_CHECK_FALED = "Node status can't be checked. HCTL command failed"
SERVICE_STATUS_CHECK_FAILED = "Service status can not be checked as services are restarting. Please check after sometime."
SHUTDOWN_NODE_FIRST =  "Please shutdown the resource first before replacing."
NODE_REPLACEMENT_ALREADY_RUNNING = "Node replacement is already in progress."
NODE_REPLACEMENT_STARTED = "Node replacement for {resource_name} started."
RESOURCE_ALREADY_SAME_STATE = "Resource is already in same state"
SHUTDOWN_COMMENT = "node_shutdown_cron"
#Services
HEALTH_SERVICE = "health_service"
ALERTS_SERVICE = "alerts_service"

ALERT_RETRY_COUNT = 3
COMMON = "common"
MAINTENANCE = "MAINTENANCE"
SUPPORT_BUNDLE_SHELL_COMMAND = "sh {cortxcli_path}/cli/schema/create_support_bundle.sh {args}"
CORTXCLI = "cortxcli"
RMQ_CLUSTER_STATUS_RETRY_COUNT = 3
SUPPORT_MSG = "alerts_support_message"
SUPPORT_DEFAULT_MSG = "Please contact CORTX community. Visit https://github.com/Seagate/cortx for details on how to contact CORTX community."
ID = "id"
CLUSTER = "cluster"
HEALTH_SCHEMA_KEY = "HEALTH>health_schema"
MINION_NODE1_ID = "srvnode-1"
MINION_NODE2_ID = "srvnode-2"
SAS_RESOURCE_TYPE = "node:interface:sas"
ACTUATOR_REQUEST_LIST = ["enclosure:hw:sideplane", "enclosure:hw:disk",
    "enclosure:hw:psu", "enclosure:hw:controller", "enclosure:hw:fan",
    "enclosure:cortx:logical_volume", "enclosure:interface:sas",
    "enclosure:sensor:current", "enclosure:sensor:temperature",
    "enclosure:sensor:voltage", "node:sensor:temperature", "node:hw:disk",
    "node:hw:psu", "node:hw:fan", "node:sensor:current", "node:sensor:voltage",
    "node:interface:sas", "node:interface:nw:cable"]
PROVISIONER_PACKAGE_NOT_INIT = "Provisioner is not instantiated."


HIGH_RISK_SEVERITY = ['critical', 'CRITICAL', 'error', 'ERROR']
GOOD_HEALTH_VAL = ['OK', 'NA', 'ok', 'na']
LOW_RISK_SEVERITY = ['warning', 'WARNING', 'NA', 'na', '', 'informational', 'INFORMATIONAL']
EDGE_INSTALL_TYPE ={ "nodes": 1,
                    "servers_per_node": 2,
                    "storage_type": ["5u84", "PODS", "RBOD"],
                    "server_type": "physical"}

#unsupported feature
UNSUPPORTED_FEATURE_SCHEMA='{}/schema/unsupported_features.json'.format(CSM_PATH)
FEATURE_ENDPOINT_MAPPING_SCHEMA = '{}/schema/feature_endpoint_mapping.json'.format(CSM_PATH)
L18N_SCHEMA = '{}/schema/l18n.json'.format(CSM_PATH)
DEPENDENT_ON = "dependent_on"
CSM_COMPONENT_NAME = "csm"
COMPONENT_NAME = "component_name"
FEATURE_NAME = "feature_name"
SETUP_TYPES = "setup_types"
TYPE = 'type'
UNSUPPORTED_FEATURES = "unsupported_features"
STORAGE_TYPE = "storage_type"
STORAGE = "storage"
STORAGE_TYPE_VIRTUAL = "virtual"
FEATURE_ENDPOINT_MAP_INDEX = "FEATURE_COMPONENTS.feature_endpoint_map"
OK = 'ok'
EMPTY_PASS_FIELD = "Password field can't be empty."
HEALTH_REQUIRED_FIELDS = {'health', 'severity', 'alert_uuid', 'alert_type'}
SHUTDOWN_CRON_TIME = "shutdown_cron_time"
ES_RETRY = "ELASTICSEARCH>retry"
ES_RECORD_LIMIT = 1000
ES_CLEANUP_PERIOD_VIRTUAL = 2  # days
LOGROTATE_AMOUNT_VIRTUAL = 3

#SSL
SUBJECT = "subject"
ISSUER = "issuer"
NOT_VALID_AFTER = "not_valid_after"
NOT_VALID_BEFORE = "not_valid_before"
SERIAL_NUMBER = "serial_number"
VERSION = "version"
SIGNATURE_ALGORITHM_OID = "signature_algorithm_oid"
CERT_DETAILS = "cert_details"

# MEssage Bus
PRODUCER_ID = 'producer_id'
MESSAGE_TYPE = 'message_type'
METHOD = 'method'
ASYNC = 'async'
CONSUMER_ID = 'consumer_id'
CONSUMER_GROUP = 'consumer_group'
CONSUMER_MSG_TYPES = 'consumer_message_types'
AUTO_ACK = 'auto_ack'
OFFSET = 'offset'
EARLIEST = 'earliest'
TYPE = 'type'
PRODUCER = 'producer'
CONSUMER = 'consumer'
CONSUMER_CALLBACK = 'consumer_callback'
BLOCKING = 'blocking'
PRODUCER_ID_KEY = 'MESSAGEBUS>PRODUCER>ACTUATOR>producer_id'
MSG_TYPE_KEY = 'MESSAGEBUS>PRODUCER>ACTUATOR>message_type'
METHOD_KEY = 'MESSAGEBUS>PRODUCER>ACTUATOR>method'
CONSUMER_ID_KEY = 'MESSAGEBUS>CONSUMER>ALERTS>consumer_id'
CONSUMER_GROUP_KEY = 'MESSAGEBUS>CONSUMER>ALERTS>consumer_group'
CONSUER_MSG_TYPES_KEY = 'MESSAGEBUS>CONSUMER>ALERTS>consumer_message_types'
CONSUMER_OFFSET = 'MESSAGEBUS>CONSUMER>ALERTS>offset'

#ConfStore Keys
KEY_DEPLOYMENT_MODE = f"{DEPLOYMENT}>{MODE}"
SERVER_NODE_INFO = f"{SERVER_NODE}>machine_id"
KEY_SERVER_NODE_INFO = "server_node_info_key"
KEY_SERVER_NODE_TYPE = "server_node_type_key"
KEY_ENCLOSURE_ID = "enclosure_id_key"
KEY_CLUSTER_ID = "cluster_id_key"
KEY_CSM_USER = "csm_user_key"
KEY_CSM_SECRET = "csm_secret_key"
KEY_S3_LDAP_USER = "openldap_s3_user_key"
KEY_S3_LDAP_SECRET = "openldap_s3_secret_key"
KEY_ROAMING_IP = "roaming_ip_key"
KEY_HOSTNAME = "node_hostname_key"
KEY_DATA_NW_PUBLIC_FQDN = "data_nw_public_fqdn"
KEY_DATA_NW_PRIVATE_FQDN = "data_nw_private_fqdn"

#CSM TEST Consts
DEFAULT_BROWSER = 'chrome'
DEFAULT_TEST_PLAN = CSM_PATH + '/test/plans/service_sanity.pln'
DEFAULT_ARG_PATH = CSM_PATH + '/test/test_data/args.yaml'
DEFAULT_LOGFILE = '/tmp/csm_gui_test.log'
DEFAULT_OUTPUTFILE = '/tmp/output.log'

#Cluster admin creds
DEFAULT_CLUSTER_ADMIN_USER = 'cortxadmin'
DEFAULT_CLUSTER_ADMIN_PASS = 'Cortxadmin@123'
DEFAULT_CLUSTER_ADMIN_EMAIL = 'cortxadmin@seagate.com'
