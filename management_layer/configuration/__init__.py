from access_control import AccessControlApi, ApiClient as AccessControlApiClient
from authentication_service import AuthenticationApi, ApiClient as AuthenticationServiceApiClient
from user_data_store import UserDataApi, ApiClient as UserDataApiClient
from management_layer.configuration.access_control import \
    Configuration as AccessControlConfiguration
from management_layer.configuration.authentication_service import \
    Configuration as AuthenticationServiceConfiguration
from management_layer.configuration.user_data_store import \
    Configuration as UserDataStoreConfiguration

# In older versions of Swagger Codegen, the client configuration was a singleton object
# which made it slightly more convenient to manage.
# For now we control the client configuration by explicitly pointing it to
# our own copies of the (modified) default configuration.
access_control_configuration = AccessControlConfiguration()
access_control_api = AccessControlApi(
    api_client=AccessControlApiClient(
        configuration=access_control_configuration
    )
)

authentication_configuration = AuthenticationServiceConfiguration()
authentication_api = AuthenticationApi(
    api_client=AuthenticationServiceApiClient(
        configuration=authentication_configuration
    )
)

user_data_store_configuration = UserDataStoreConfiguration()
user_data_api = UserDataApi(
    api_client=UserDataApiClient(
        configuration=user_data_store_configuration
    )
)
