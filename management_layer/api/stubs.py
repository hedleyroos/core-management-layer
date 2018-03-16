"""
Do not modify this file. It is generated from the Swagger specification.
"""
import json
from apitools.datagenerator import DataGenerator

import management_layer.api.schemas as schemas


class AbstractStubClass(object):
    """
    Implementations need to be derived from this class.
    """

    @staticmethod
    async def adminnote_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param creator_id (optional): string An optional query parameter to filter by creator (a user_id)
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_delete(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_read(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def adminnote_update(request, body, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def client_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param client_ids (optional): array An optional list of client ids
        :param client_id (optional): string An optional client id to filter on. This is not the primary key.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def client_read(request, client_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_id: string A string value identifying the client
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domainrole_delete(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domainrole_read(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domainrole_update(request, body, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_ids (optional): array An optional list of domain ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_delete(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_read(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def domain_update(request, body, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitation_id (optional): string An optional query parameter to filter by invitation_id
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_delete(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_read(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitor_id (optional): string Optional filter based on the invitor (the user who created the invitation)
        :param invitation_ids (optional): array An optional list of invitation ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_delete(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_read(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_update(request, body, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitation_id (optional): string An optional query parameter to filter by invitation_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_delete(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_read(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get_all_user_roles(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get_domain_roles(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get_site_and_domain_roles(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get_site_role_labels_aggregated(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get_user_site_role_labels_aggregated(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param permission_ids (optional): array An optional list of permission ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_delete(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_read(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_update(request, body, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param prefix (optional): string An optional URN prefix filter
        :param resource_ids (optional): array An optional list of resource ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_delete(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_read(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def resource_update(request, body, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :param resource_id (optional): integer An optional resource filter
        :param permission_id (optional): integer An optional permission filter
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_delete(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def roleresourcepermission_read(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def role_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_ids (optional): array An optional list of role ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def role_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def role_delete(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def role_read(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def role_update(request, body, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def sitedataschema_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_delete(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_read(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def siterole_update(request, body, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def site_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def site_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def site_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def site_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def site_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_sites_site_id_activate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_sites_site_id_deactivate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_delete(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def userdomainrole_read(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def user_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param email (optional): string An optional email filter
        :param username_prefix (optional): string An optional username prefix filter
        :param user_ids (optional): array An optional list of user ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def user_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def user_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def user_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_users_user_id_activate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_users_user_id_deactivate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersitedata_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersiterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersiterole_delete(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    @staticmethod
    async def usersiterole_read(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()


class MockedStubClass(AbstractStubClass):
    """
    Provides a mocked implementation of the AbstractStubClass.
    """
    GENERATOR = DataGenerator()


    @staticmethod
    async def adminnote_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param creator_id (optional): string An optional query parameter to filter by creator (a user_id)
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "creator_id": {
                "description": "The user making the request will be considered the creator and thus this field is not available when creating admin note.",
                "format": "uuid",
                "readOnly": true,
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "note": {
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "id",
            "user_id",
            "creator_id",
            "note",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def adminnote_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.admin_note
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def adminnote_delete(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def adminnote_read(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        """
        response_schema = schemas.admin_note
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def adminnote_update(request, body, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param admin_note_id: integer A unique integer value identifying the admin note.
        """
        response_schema = schemas.admin_note
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def client_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param client_ids (optional): array An optional list of client ids
        :param client_id (optional): string An optional client id to filter on. This is not the primary key.
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "_post_logout_redirect_uris": {
                "description": "New-line delimited list of post-logout redirect URIs",
                "type": "string"
            },
            "_redirect_uris": {
                "description": "New-line delimited list of redirect URIs",
                "type": "string"
            },
            "client_id": {
                "description": "",
                "type": "string"
            },
            "contact_email": {
                "description": "",
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "logo": {
                "description": "",
                "format": "uri",
                "type": "string"
            },
            "name": {
                "description": "",
                "type": "string"
            },
            "require_consent": {
                "description": "If disabled, the Server will NEVER ask the user for consent.",
                "type": "boolean"
            },
            "response_type": {
                "description": "",
                "type": "string"
            },
            "reuse_consent": {
                "description": "If enabled, the Server will save the user consent given to a specific client, so that user will not be prompted for the same authorization multiple times.",
                "type": "boolean"
            },
            "terms_url": {
                "description": "External reference to the privacy policy of the client.",
                "type": "string"
            },
            "website_url": {
                "description": "",
                "type": "string"
            }
        },
        "required": [
            "id",
            "client_id",
            "response_type"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def client_read(request, client_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_id: string A string value identifying the client
        """
        response_schema = schemas.client
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "grant_implicitly": {
                "type": "boolean"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "domain_id",
            "role_id",
            "grant_implicitly",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domainrole_delete(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domainrole_read(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domainrole_update(request, body, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domain_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_ids (optional): array An optional list of domain ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "name": {
                "maxLength": 100,
                "type": "string"
            },
            "parent_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "name",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domain_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.domain
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domain_delete(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domain_read(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        response_schema = schemas.domain
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def domain_update(request, body, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        """
        response_schema = schemas.domain
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationdomainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitation_id (optional): string An optional query parameter to filter by invitation_id
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "invitation_id": {
                "format": "uuid",
                "type": "string"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "invitation_id",
            "domain_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.invitation_domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationdomainrole_delete(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationdomainrole_read(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.invitation_domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitation_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitor_id (optional): string Optional filter based on the invitor (the user who created the invitation)
        :param invitation_ids (optional): array An optional list of invitation ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "email": {
                "format": "email",
                "type": "string"
            },
            "expires_at": {
                "format": "date-time",
                "type": "string"
            },
            "first_name": {
                "maxLength": 100,
                "type": "string"
            },
            "id": {
                "format": "uuid",
                "readOnly": true,
                "type": "string"
            },
            "invitor_id": {
                "description": "The user that created the invitation",
                "format": "uuid",
                "type": "string"
            },
            "last_name": {
                "maxLength": 100,
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "invitor_id",
            "first_name",
            "last_name",
            "email",
            "expires_at",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.invitation
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitation_delete(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitation_read(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        """
        response_schema = schemas.invitation
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitation_update(request, body, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitation_id: string A UUID value identifying the invitation.
        """
        response_schema = schemas.invitation
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationsiterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitation_id (optional): string An optional query parameter to filter by invitation_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "invitation_id": {
                "format": "uuid",
                "type": "string"
            },
            "role_id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "invitation_id",
            "site_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationsiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.invitation_site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationsiterole_delete(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationsiterole_read(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.invitation_site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_all_user_roles(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.all_user_roles
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_domain_roles(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        response_schema = schemas.domain_roles
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_site_and_domain_roles(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.site_and_domain_roles
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_site_role_labels_aggregated(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.site_role_labels_aggregated
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_user_site_role_labels_aggregated(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.user_site_role_labels_aggregated
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def permission_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param permission_ids (optional): array An optional list of permission ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "name": {
                "maxLength": 50,
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "name",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def permission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.permission
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def permission_delete(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def permission_read(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        """
        response_schema = schemas.permission
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def permission_update(request, body, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param permission_id: integer A unique integer value identifying the permission.
        """
        response_schema = schemas.permission
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def resource_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param prefix (optional): string An optional URN prefix filter
        :param resource_ids (optional): array An optional list of resource ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "urn": {
                "format": "uri",
                "type": "string"
            }
        },
        "required": [
            "id",
            "urn",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def resource_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.resource
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def resource_delete(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def resource_read(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        """
        response_schema = schemas.resource
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def resource_update(request, body, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param resource_id: integer A unique integer value identifying the resource.
        """
        response_schema = schemas.resource
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def roleresourcepermission_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :param resource_id (optional): integer An optional resource filter
        :param permission_id (optional): integer An optional permission filter
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "permission_id": {
                "type": "integer"
            },
            "resource_id": {
                "type": "integer"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "role_id",
            "resource_id",
            "permission_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def roleresourcepermission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.role_resource_permission
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def roleresourcepermission_delete(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def roleresourcepermission_read(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        """
        response_schema = schemas.role_resource_permission
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def role_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_ids (optional): array An optional list of role ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "label": {
                "maxLength": 100,
                "type": "string",
                "x-scope": [
                    "",
                    "#/definitions/role"
                ]
            },
            "requires_2fa": {
                "type": "boolean"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "label",
            "requires_2fa",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def role_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def role_delete(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def role_read(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def role_update(request, body, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def sitedataschema_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "schema": {
                "type": "object"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "site_id",
            "schema",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def sitedataschema_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.site_data_schema
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def sitedataschema_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def sitedataschema_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.site_data_schema
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def sitedataschema_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.site_data_schema
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def siterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "grant_implicitly": {
                "type": "boolean"
            },
            "role_id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "site_id",
            "role_id",
            "grant_implicitly",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def siterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def siterole_delete(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def siterole_read(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def siterole_update(request, body, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def site_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "client_id": {
                "format": "uuid",
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "is_active": {
                "type": "boolean"
            },
            "name": {
                "maxLength": 100,
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "domain_id",
            "name",
            "is_active",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def site_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def site_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def site_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def site_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get__api_v1_sites_site_id_activate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get__api_v1_sites_site_id_deactivate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def userdomainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "user_id",
            "domain_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def userdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.user_domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def userdomainrole_delete(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def userdomainrole_read(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.user_domain_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def user_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param email (optional): string An optional email filter
        :param username_prefix (optional): string An optional username prefix filter
        :param user_ids (optional): array An optional list of user ids
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "avatar": {
                "format": "uri",
                "type": "string"
            },
            "birth_date": {
                "format": "date",
                "type": "string"
            },
            "country_code": {
                "maxLength": 2,
                "minLength": 2,
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "date_joined": {
                "description": "",
                "format": "date",
                "readOnly": true,
                "type": "string"
            },
            "email": {
                "description": "",
                "format": "email",
                "type": "string"
            },
            "email_verified": {
                "type": "boolean"
            },
            "first_name": {
                "description": "",
                "type": "string"
            },
            "gender": {
                "type": "string"
            },
            "id": {
                "description": "The UUID of the user",
                "format": "uuid",
                "readOnly": true,
                "type": "string"
            },
            "is_active": {
                "description": "Designates whether this user should be treated as active. Deselect this instead of deleting accounts.",
                "type": "boolean"
            },
            "last_login": {
                "description": "",
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "last_name": {
                "description": "",
                "type": "string"
            },
            "msisdn": {
                "maxLength": 15,
                "type": "string"
            },
            "msisdn_verified": {
                "type": "boolean"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "username": {
                "description": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "username",
            "is_active",
            "date_joined",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def user_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def user_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.user
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def user_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get__api_v1_users_user_id_activate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get__api_v1_users_user_id_deactivate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersitedata_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "blocked": {
                "type": "boolean"
            },
            "consented_at": {
                "format": "date-time",
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "data": {
                "type": "object"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "user_id",
            "site_id",
            "consented_at",
            "blocked",
            "data",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.user_site_data
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersitedata_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersitedata_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.user_site_data
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersitedata_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.user_site_data
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersiterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "role_id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "user_id",
            "site_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.user_site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersiterole_delete(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def usersiterole_read(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        response_schema = schemas.user_site_role
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)
