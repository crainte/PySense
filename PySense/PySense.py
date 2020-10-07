from PySense import PySenseAuthentication
from PySense import PySenseException
from PySense import PySenseRestConnector
from PySense import SisenseRole
from PySense import SisenseVersion

from PySense.PySenseMixIns import BrandingMixIn
from PySense.PySenseMixIns import ConnectionMixIn
from PySense.PySenseMixIns import DashboardMixIn
from PySense.PySenseMixIns import DataModelMixIn
from PySense.PySenseMixIns import ElasticubeMixIn
from PySense.PySenseMixIns import FolderMixIn
from PySense.PySenseMixIns import GroupMixIn
from PySense.PySenseMixIns import RoleMixIn
from PySense.PySenseMixIns import PluginMixIn
from PySense.PySenseMixIns import UserMixIn


def authenticate_by_token(host, token, version, debug=False, verify=True):
    """Creates a new PySense client with the token

    Args:
        - host: The Sisense server address
        - token: A Sisense user token
        - version: 'Windows' or 'Linux'
        - debug: (Optional) True to enable debugging. False by default.
        - verify: (Optional) False to disable SSL certificate verification. True by default.


    Returns:
        A new PySense client for the given credentials
    """
    return PySenseAuthentication.authenticate_by_token(host, token, version, debug, verify)


def authenticate_by_password(host, username, password, version, debug=False, verify=True):
    """Creates a new PySense client with the username and password

    Args:
        - host: The Sisense server address
        - username: Sisense username
        - password: Sisense password
        - version: 'Windows' or 'Linux'
        - debug: (Optional) True to enable debugging. False by default.
        - verify: (Optional) False to disable SSL certificate verification. True by default.


    Returns:
        A new PySense client for the given credentials
    """
    return PySenseAuthentication.authenticate_by_password(host, username, password, version, debug, verify)


def authenticate_by_file(config_file):
    """Creates a new PySense client with the credentials in the given config file.

    py_client = PySense.authenticate_by_file('C:\\PySense\\PySenseConfig.yaml')

    See sample config in Snippets/SampleConfig.yaml

    Args:
        config_file: Yaml file with credentials

    Returns:
        A new PySense client for the given credentials
    """
    return PySenseAuthentication.authenticate_by_file(config_file)


class PySense(BrandingMixIn.BrandingMixIn, ConnectionMixIn.ConnectionMixIn, DashboardMixIn.DashboardMixIn,
              DataModelMixIn.DataModelMixIn, ElasticubeMixIn.ElasticubeMixIn, FolderMixIn.FolderMixIn,
              GroupMixIn.GroupMixIn, PluginMixIn.PluginMixIn, RoleMixIn.RoleMixIn, UserMixIn.UserMixIn):

    """The manager of connections to the PySense server

    This class is for sever level changes like getting, adding, and removing dashboards, elasticubes, users, etc

    Attributes:
        connector: The PySenseRestConnector which runs the rest commands.
    """

    def __init__(self, host, token, version, *, debug=False, verify=True, param_dict=None):
        """ Initializes a PySense instance

        Args:
            host: host address
            token: a json bearer token with format
                {'authorization':  "Bearer yourlongaccesstokenstringthatyougotfromapreviouslogin"}
            version: version (either 'Windows' or 'Linux')
            debug: If true, prints detailed REST API logs to console. False by default.
            verify: If false, disables SSL Certification. True by default.
            param_dict: For passing in additional parameters
        """
        if param_dict is None:
            self.param_dict = {}
        else:
            self.param_dict = {}

        default_dict = {
            'CUBE_CACHE_TIMEOUT_SECONDS': 60
        }

        for key, value in default_dict.items():
            if key not in self.param_dict:
                self.param_dict[key] = value

        # Verify version
        if version.lower() == 'windows':
            self.version = SisenseVersion.Version.WINDOWS
        elif version.lower() == 'linux':
            self.version = SisenseVersion.Version.LINUX
        else:
            raise PySenseException.PySenseException('{} not a valid OS. Please select Linux or Windows'.format(version))

        # Initiate PySense Connection
        self.connector = PySenseRestConnector.RestConnector(host, token, debug, verify)

        # Set up Roles
        roles = self.connector.rest_call('get', 'api/roles')
        self._roles = {}
        for role in roles:
            if role['name'] in ['dataDesigner', 'super', 'dataAdmin', 'admin', 'contributor', 'consumer']:
                self._roles[SisenseRole.Role.from_str(role['name'])] = role['_id']

    def set_debug(self, debug):
        """Enable or disable logging of REST api calls to std out.

        Use for debugging. Debug is false by default.
        """
        self.connector.debug = debug

    def get_param(self, param):
        """Get the value in the param dictionary for the given parameter. Returns None if not found"""
        if param in self.param_dict:
            return self.param_dict[param]
        else:
            None

    def set_param(self, param, value):
        """Set the key "param" to the value "value". """
        self.param_dict[param] = value
