from management_layer.api.stubs import AbstractStubClass
from authentication_service.api.authentication_api import AuthenticationApi
from user_data_store.api.user_data_api import UserDataApi
from access_control.api.access_control_api import AccessControlApi
from management_layer import transformations

authentication_api = AuthenticationApi()
user_data_api = UserDataApi()
access_control_api = AccessControlApi()

# An example of using aiobravado for API clients.
# Do not remove yet. (cobusc)

# from aiobravado.client import SwaggerClient
# from aiobravado.swagger_model import load_file
# async def get_client():
#     spec = await load_file("../core-access-control/swagger/access_control.yml")
#     client = SwaggerClient.from_spec(spec, config={"use_models": False})
#     return client
#
# client = asyncio.get_event_loop().run_until_complete(get_client())


class Implementation(AbstractStubClass):
    """
    The implementation linking calls made the Management Layer
    to the Authentication-, Access Control- and User Data Store services.
    """

    @staticmethod
    async def adminnote_list(request, offset=None, limit=None, user_id=None, creator_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param creator_id (optional): string An optional query parameter to filter by creator (a user_id)
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_delete(request, user_id, creator_id, created_at, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param creator_id: string The creator_id
        :param created_at: string The created_at value
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_read(request, user_id, creator_id, created_at, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param creator_id: string The creator_id
        :param created_at: string The created_at value
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_update(request, body, user_id, creator_id, created_at, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param creator_id: string The creator_id
        :param created_at: string The created_at value
        """
        raise NotImplementedError()

    @staticmethod
    async def client_list(request, offset=None, limit=None, client_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param client_ids (optional): array An optional list of client ids
        """
        raise NotImplementedError()

    @staticmethod
    async def client_read(request, client_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param client_id: string A UUID value identifying the client
        """
        raise NotImplementedError()

    @staticmethod
    async def domainrole_list(request, offset=None, limit=None, domain_id=None, role_id=None, *args, **params):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        params = {}
        if offset:
            params["offset"] = int(offset)
        if limit:
            params["limit"] = int(limit)
        if domain_id:
            params["domain_id"] = domain_id
        if role_id:
            params["role_id"] = role_id
        domain_roles = await access_control_api.domainrole_list(**params)
        if domain_roles:
            transform = transformations.DOMAIN_ROLE
            result = [transform.apply(dr.to_dict()) for dr in domain_roles]
            return result

        return []

    @staticmethod
    async def domainrole_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        domain_role = await access_control_api.domainrole_create(data=body)
        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    @staticmethod
    async def domainrole_delete(request, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        result = await access_control_api.domainrole_delete(domain_id, role_id)
        return result

    @staticmethod
    async def domainrole_read(request, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        domain_role = await access_control_api.domainrole_read(domain_id, role_id)
        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    @staticmethod
    async def domainrole_update(request, body, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        domain_role = await access_control_api.domainrole_update(domain_id, role_id, data=body)
        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    @staticmethod
    async def domain_list(request, offset=None, limit=None, domain_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_ids (optional): array An optional list of domain ids
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_delete(request, domain_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_read(request, domain_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_update(request, body, domain_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_list(request, offset=None, limit=None, invitation_id=None, domain_id=None, role_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitation_id (optional): string An optional query parameter to filter by invitation_id
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_delete(request, invitation_id, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_read(request, invitation_id, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_list(request, offset=None, limit=None, invitor_id=None, invitation_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitor_id (optional): string Optional filter based on the invitor (the user who created the invitation)
        :param invitation_ids (optional): array An optional list of invitation ids
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_delete(request, invitation_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_read(request, invitation_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_update(request, body, invitation_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitation_id: string A UUID value identifying the invitation.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_list(request, offset=None, limit=None, invitation_id=None, site_id=None, role_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitation_id (optional): string An optional query parameter to filter by invitation_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_delete(request, invitation_id, site_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_read(request, invitation_id, site_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_all_user_roles(request, user_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_domain_roles(request, domain_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_site_and_domain_roles(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_site_role_labels_aggregated(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_user_site_role_labels_aggregated(request, user_id, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_list(request, offset=None, limit=None, permission_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param permission_ids (optional): array An optional list of permission ids
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_delete(request, permission_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_read(request, permission_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_update(request, body, permission_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param permission_id: integer A unique integer value identifying the permission.
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_list(request, offset=None, limit=None, prefix=None, resource_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param prefix (optional): string An optional URN prefix filter
        :param resource_ids (optional): array An optional list of resource ids
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_delete(request, resource_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_read(request, resource_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_update(request, body, resource_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param resource_id: integer A unique integer value identifying the resource.
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_list(request, offset=None, limit=None, role_id=None, resource_id=None, permission_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :param resource_id (optional): integer An optional resource filter
        :param permission_id (optional): integer An optional permission filter
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_delete(request, role_id, resource_id, permission_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_read(request, role_id, resource_id, permission_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        """
        raise NotImplementedError()

    @staticmethod
    async def role_list(request, offset=None, limit=None, role_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_ids (optional): array An optional list of role ids
        """
        raise NotImplementedError()

    @staticmethod
    async def role_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def role_delete(request, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def role_read(request, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def role_update(request, body, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_list(request, offset=None, limit=None, site_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_delete(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_read(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_update(request, body, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_list(request, offset=None, limit=None, site_id=None, role_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_delete(request, site_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_read(request, site_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_update(request, body, site_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def site_list(request, offset=None, limit=None, site_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        """
        raise NotImplementedError()

    @staticmethod
    async def site_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def site_delete(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def site_read(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def site_update(request, body, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_sites_site_id_activate(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_sites_site_id_deactivate(request, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_list(request, offset=None, limit=None, user_id=None, domain_id=None, role_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_delete(request, user_id, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_read(request, user_id, domain_id, role_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def user_list(request, offset=None, limit=None, email=None, user_ids=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param email (optional): string An optional email filter
        :param user_ids (optional): array An optional list of user ids
        """
        raise NotImplementedError()

    @staticmethod
    async def user_delete(request, user_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def user_read(request, user_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def user_update(request, body, user_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_users_user_id_activate(request, user_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_users_user_id_deactivate(request, user_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_list(request, offset=None, limit=None, user_id=None, site_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_delete(request, user_id, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_read(request, user_id, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_update(request, body, user_id, site_id, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def usersiterole_list(request, offset=None, limit=None, user_id=None, site_id=None, role_id=None, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        raise NotImplementedError()

    @staticmethod
    async def usersiterole_create(request, body, *args, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

