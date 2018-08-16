import datetime
import logging
import socket
import uuid

from management_layer.api.stubs import AbstractStubClass
from management_layer.exceptions import JSONBadRequest, JSONForbidden, JSONNotFound
from management_layer import transformations, mappings, __version__, settings
from management_layer.constants import TECH_ADMIN_ROLE_LABEL
from management_layer.permission import utils
from management_layer.permission.decorator import require_permissions, requester_has_role
from management_layer.settings import MANAGEMENT_PORTAL_CLIENT_ID
from management_layer.utils import client_exception_handler, transform_users_with_roles

TOTAL_COUNT_HEADER = "X-Total-Count"
CLIENT_TOTAL_COUNT_HEADER = "X-Total-Count"

logger = logging.getLogger(__name__)


class Implementation(AbstractStubClass):
    """
    The implementation linking calls made the Management Layer
    to the Authentication-, Access Control- and User Data Store services.
    """

    # adminnote_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:adminnote", "read")],
                         target_user_field="creator_id")
    async def adminnote_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param creator_id (optional): string An optional query parameter to filter by creator (a user_id)
        :param admin_note_ids (optional): array An optional list of adminnote ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            admin_notes, _status, headers = await request.app[
                "user_data_api"].adminnote_list_with_http_info(**kwargs)

        if admin_notes:
            transform = transformations.ADMIN_NOTE
            admin_notes = [transform.apply(note.to_dict()) for note in admin_notes]
        return admin_notes, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # adminnote_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:adminnote", "create")])
    async def adminnote_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        # The caller of this function is considered the creator.
        body["creator_id"] = request["token"]["sub"]

        with client_exception_handler():
            admin_note = await request.app["user_data_api"].adminnote_create(admin_note_create=body)

        if admin_note:
            transform = transformations.ADMIN_NOTE
            return transform.apply(admin_note.to_dict())

        return None

    # adminnote_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:adminnote", "delete")])
    async def adminnote_delete(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["user_data_api"].adminnote_delete(admin_note_id)

        return result

    # adminnote_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:adminnote", "read")])
    async def adminnote_read(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            admin_note = await request.app["user_data_api"].adminnote_read(admin_note_id)

        if admin_note:
            transform = transformations.ADMIN_NOTE
            return transform.apply(admin_note.to_dict())

        return None

    # adminnote_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:adminnote", "update")])
    async def adminnote_update(request, body, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            admin_note = await request.app["user_data_api"].adminnote_update(admin_note_id,
                                                                             admin_note_update=body)

        if admin_note:
            transform = transformations.ADMIN_NOTE
            return transform.apply(admin_note.to_dict())

        return None

    # client_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:identity_provider:oidc_provider:client", "read")])
    async def client_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param client_ids (optional): array An optional list of client ids
        :param client_token_id (optional): string An optional client id to filter on. This is not the primary key.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            clients, _status, headers = await request.app[
                "authentication_service_api"].client_list_with_http_info(**kwargs)

        if clients:
            transform = transformations.CLIENT
            clients = [transform.apply(client.to_dict()) for client in clients]

        return clients, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # client_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:identity_provider:oidc_provider:client", "read")])
    async def client_read(request, client_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_id: integer A integer identifying the client
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            client = await request.app["authentication_service_api"].client_read(client_id)

        if client:
            transform = transformations.CLIENT
            result = transform.apply(client.to_dict())
            return result

        return None

    # country_list -- Synchronisation point for meld
    @staticmethod
    # No permissions are required for this
    async def country_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param country_codes (optional): array An optional list of country codes
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            countries, _status, headers = await request.app[
                "authentication_service_api"].country_list_with_http_info(**kwargs)

        if countries:
            transform = transformations.COUNTRY
            countries = [transform.apply(country.to_dict()) for country in countries]

        return countries, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # country_read -- Synchronisation point for meld
    @staticmethod
    # No permissions are required for this
    async def country_read(request, country_code, **kwargs):
        """
        :param request: An HttpRequest
        :param country_code: string A unique two-character value identifying the country.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            country = await request.app["authentication_service_api"].country_read(country_code)

        if country:
            transform = transformations.COUNTRY
            result = transform.apply(country.to_dict())
            return result

        return None

    # deleteduser_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deleteduser", "read")])
    async def deleteduser_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param deleter_id (optional): string An optional query parameter to filter by deleter_id
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_users, _status, headers = await request.app[
                "user_data_api"].deleteduser_list_with_http_info(**kwargs)

        if deleted_users:
            transform = transformations.DELETED_USER
            deleted_users = [transform.apply(deleted_user.to_dict())
                             for deleted_user in deleted_users]

        return deleted_users, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # deleteduser_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deleteduser", "create")])
    async def deleteduser_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        # The caller of this function is considered the deleter.
        body["deleter_id"] = request["token"]["sub"]

        with client_exception_handler():
            deleted_user = await request.app["user_data_api"].deleteduser_create(
                deleted_user_create=body)

        if deleted_user:
            transform = transformations.DELETED_USER
            return transform.apply(deleted_user.to_dict())

        return None

    # deleteduser_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deleteduser", "delete")])
    async def deleteduser_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["user_data_api"].deleteduser_delete(user_id)

        return result

    # deleteduser_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deleteduser", "read")])
    async def deleteduser_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_user = await request.app["user_data_api"].deleteduser_read(user_id)

        if deleted_user:
            transform = transformations.DELETED_USER
            result = transform.apply(deleted_user.to_dict())
            return result

        return None

    # deleteduser_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deleteduser", "update")])
    async def deleteduser_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_user = await request.app["user_data_api"].deleteduser_update(
                user_id, deleted_user_update=body)

        if deleted_user:
            transform = transformations.DELETED_USER
            return transform.apply(deleted_user.to_dict())

        return None

    # deletedusersite_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deletedusersite", "read")])
    async def deletedusersite_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_user_sites, _status, headers = await request.app[
                "user_data_api"].deletedusersite_list_with_http_info(**kwargs)

        if deleted_user_sites:
            transform = transformations.DELETED_USER_SITE
            deleted_user_sites = [transform.apply(deleted_user_site.to_dict())
                                  for deleted_user_site in deleted_user_sites]

        return deleted_user_sites, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # deletedusersite_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deletedusersite", "create")])
    async def deletedusersite_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_user_site = await request.app["user_data_api"].deletedusersite_create(
                deleted_user_site_create=body)

        if deleted_user_site:
            transform = transformations.DELETED_USER_SITE
            return transform.apply(deleted_user_site.to_dict())

        return None

    # deletedusersite_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deletedusersite", "delete")])
    async def deletedusersite_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["user_data_api"].deletedusersite_delete(user_id, site_id)

        return result

    # deletedusersite_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deletedusersite", "read")])
    async def deletedusersite_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_user_site = await request.app[
                "user_data_api"].deletedusersite_read(user_id, site_id)

        if deleted_user_site:
            transform = transformations.DELETED_USER_SITE
            result = transform.apply(deleted_user_site.to_dict())
            return result

        return None

    # deletedusersite_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:deletedusersite", "update")])
    async def deletedusersite_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            deleted_user_site = await request.app["user_data_api"].deletedusersite_update(
                user_id, site_id, deleted_user_site_update=body)

        if deleted_user_site:
            transform = transformations.DELETED_USER_SITE
            return transform.apply(deleted_user_site.to_dict())

        return None

    # domainrole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domainrole", "read")])
    async def domainrole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_id (optional): integer An optional query parameter to filter by domain_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain_roles, _status, headers = await request.app[
                "access_control_api"].domainrole_list_with_http_info(**kwargs)

        if domain_roles:
            transform = transformations.DOMAIN_ROLE
            domain_roles = [transform.apply(domain_role.to_dict()) for domain_role in domain_roles]

        return domain_roles, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # domainrole_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domainrole", "create")])
    async def domainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain_role = await request.app["access_control_api"].domainrole_create(
                domain_role_create=body)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    # domainrole_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domainrole", "delete")])
    async def domainrole_delete(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].domainrole_delete(domain_id, role_id)

        return result

    # domainrole_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domainrole", "read")])
    async def domainrole_read(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain_role = await request.app["access_control_api"].domainrole_read(domain_id, role_id)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    # domainrole_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domainrole", "update")])
    async def domainrole_update(request, body, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain_role = await request.app["access_control_api"].domainrole_update(
                domain_id, role_id, domain_role_update=body)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    # domain_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read")],
                         allow_for_management_portal=True)
    async def domain_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param parent_id (optional): integer An optional query parameter to filter by parent_id
        :param domain_ids (optional): array An optional list of domain ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domains, _status, headers = await request.app[
                "access_control_api"].domain_list_with_http_info(**kwargs)

        if domains:
            transform = transformations.DOMAIN
            domains = [transform.apply(domain.to_dict()) for domain in domains]

        return domains, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # domain_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "create")])
    async def domain_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain = await request.app["access_control_api"].domain_create(domain_create=body)

        if domain:
            transform = transformations.DOMAIN
            result = transform.apply(domain.to_dict())
            return result

        return None

    # domain_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "delete")])
    async def domain_delete(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].domain_delete(domain_id)

        return result

    # domain_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read")],
                         allow_for_management_portal=True)
    async def domain_read(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain = await request.app["access_control_api"].domain_read(domain_id)

        if domain:
            transform = transformations.DOMAIN
            result = transform.apply(domain.to_dict())
            return result

        return None

    # domain_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "update")])
    async def domain_update(request, body, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain = await request.app["access_control_api"].domain_update(domain_id,
                                                                           domain_update=body)

        if domain:
            transform = transformations.DOMAIN
            result = transform.apply(domain.to_dict())
            return result

        return None

    # healthcheck -- Synchronisation point for meld
    @staticmethod
    async def healthcheck(request, **kwargs):
        """
        The healthcheck for the Management Layer simply returns a structure
        with the version, timestamp and host name.
        The health statuses of the backends have been included as well, although
        they have no effect on whether the management layer is considered healthy
        or not on its own.
        :param request: An HttpRequest
        :returns: result or (result, headers) tuple
        """
        try:
            access_control_health = await request.app["operational_api"].healthcheck()
            access_control_health = access_control_health.to_dict()
            for field in ["server_timestamp", "db_timestamp"]:
                access_control_health[field] = access_control_health[field].isoformat()
        except Exception as e:
            access_control_health = {"error": str(e)}

        try:
            user_data_store_health = await request.app["user_data_api"].healthcheck()
            user_data_store_health = user_data_store_health.to_dict()
            for field in ["server_timestamp", "db_timestamp"]:
                user_data_store_health[field] = user_data_store_health[field].isoformat()
        except Exception as e:
            user_data_store_health = {"error": str(e)}

        try:
            url = settings.AUTHENTICATION_SERVICE_API + "/healthcheck"
            async with request.app["client_session"].get(url) as resp:
                authentication_service_health = await resp.json()
        except Exception as e:
            authentication_service_health = {"error": str(e)}

        result = {
            "host": socket.getfqdn(),
            "server_timestamp": datetime.datetime.now().isoformat(),
            "version": __version__,
            "access_control_health": access_control_health,
            "user_data_store_health": user_data_store_health,
            "authentication_service_health": authentication_service_health
        }
        return result

    # invitationdomainrole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationdomainrole", "read")])
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
        with client_exception_handler():
            invitation_domain_roles, _status, headers = await request.app[
                "access_control_api"].invitationdomainrole_list_with_http_info(**kwargs)

        if invitation_domain_roles:
            transform = transformations.INVITATION_DOMAIN_ROLE
            invitation_domain_roles = [transform.apply(invitation_domain_role.to_dict())
                                       for invitation_domain_role in invitation_domain_roles]

        return invitation_domain_roles, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # invitationdomainrole_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationdomainrole", "create")])
    @requester_has_role(body_field=1)
    async def invitationdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitation_domain_role = await request.app[
                "access_control_api"].invitationdomainrole_create(
                invitation_domain_role_create=body)

        if invitation_domain_role:
            transform = transformations.INVITATION_DOMAIN_ROLE
            result = transform.apply(invitation_domain_role.to_dict())
            return result

        return None

    # invitationdomainrole_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationdomainrole", "delete")])
    @requester_has_role(target_invitation_id_field=1, domain_id_field=2, role_id_field=3)
    async def invitationdomainrole_delete(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].invitationdomainrole_delete(
                invitation_id=invitation_id, domain_id=domain_id, role_id=role_id)

        return result

    # invitationdomainrole_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationdomainrole", "read")])
    async def invitationdomainrole_read(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitation_domain_role = await request.app[
                "access_control_api"].invitationdomainrole_read(
                invitation_id=invitation_id, domain_id=domain_id, role_id=role_id)

        if invitation_domain_role:
            transform = transformations.INVITATION_DOMAIN_ROLE
            result = transform.apply(invitation_domain_role.to_dict())
            return result

        return None

    # invitation_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitation", "read")])
    async def invitation_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitor_id (optional): string Optional filter based on the invitor (the user who created the invitation)
        :param invitation_ids (optional): array An optional list of invitation ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitations, _status, headers = await request.app[
                "access_control_api"].invitation_list_with_http_info(**kwargs)

        if invitations:
            transform = transformations.INVITATION
            invitations = [transform.apply(invitation.to_dict()) for invitation in invitations]

        return invitations, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # invitation_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitation", "create")])
    async def invitation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        # The caller of this function is considered the invitor.
        body["invitor_id"] = request["token"]["sub"]

        with client_exception_handler():
            invitation = await request.app["access_control_api"].invitation_create(
                invitation_create=body)

        if invitation:
            transform = transformations.INVITATION
            result = transform.apply(invitation.to_dict())
            return result

        return None

    # invitation_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitation", "delete")])
    async def invitation_delete(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].invitation_delete(invitation_id)

        return result

    # invitation_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitation", "read")])
    async def invitation_read(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitation = await request.app["access_control_api"].invitation_read(invitation_id)

        if invitation:
            transform = transformations.INVITATION
            result = transform.apply(invitation.to_dict())
            return result

        return None

    # invitation_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitation", "update")])
    async def invitation_update(request, body, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitation = await request.app["access_control_api"].invitation_update(
                invitation_id, invitation_update=body)

        if invitation:
            transform = transformations.INVITATION
            result = transform.apply(invitation.to_dict())
            return result

        return None

    # invitation_send -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitation", "read")])
    async def invitation_send(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string
        :param language (optional): string
        :returns: result or (result, headers) tuple
        """
        language = kwargs.get("language", "en")
        with client_exception_handler():
            # Note that invitations are sent by the Authentication Service and not
            # the Access Control component.
            result = await request.app[
                "authentication_service_api"].invitation_send(invitation_id, language=language)

        return result

    # purge_expired_invitations -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def purge_expired_invitations(request, **kwargs):
        """
        :param request: An HttpRequest
        :param synchronous_mode (optional): boolean Change the mode of the call to synchronous.
        :param cutoff_date (optional): string An optional cutoff date to purge invites before this date
        :returns: result or (result, headers) tuple
        """
        synchronous_mode = kwargs.get("synchronous_mode", False)
        cutoff_date = kwargs.get("cutoff_date", None)
        with client_exception_handler():
            request_kwargs = {
                "cutoff_date": cutoff_date
            } if cutoff_date else {}
            api = "operational_api" if synchronous_mode else "authentication_service_api"
            response = await request.app[api].purge_expired_invitations(**request_kwargs)
            purged_invitations = response.to_dict() if synchronous_mode else {}
            purged_invitations["mode"] = "synchronous" if synchronous_mode else "asynchronous"
            return purged_invitations

    # invitationsiterole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationsiterole", "read")])
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
        with client_exception_handler():
            invitation_site_roles, _status, headers = await request.app[
                "access_control_api"].invitationsiterole_list_with_http_info(**kwargs)

        if invitation_site_roles:
            transform = transformations.INVITATION_SITE_ROLE
            invitation_site_roles = [transform.apply(invitation_site_role.to_dict())
                                     for invitation_site_role in invitation_site_roles]

        return invitation_site_roles, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # invitationsiterole_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationsiterole", "create")])
    @requester_has_role(body_field=1)
    async def invitationsiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitation_site_role = await request.app[
                "access_control_api"].invitationsiterole_create(invitation_site_role_create=body)

        if invitation_site_role:
            transform = transformations.INVITATION_SITE_ROLE
            result = transform.apply(invitation_site_role.to_dict())
            return result

        return None

    # invitationsiterole_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationsiterole", "delete")])
    @requester_has_role(target_invitation_id_field=1, site_id_field=2, role_id_field=3)
    async def invitationsiterole_delete(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].invitationsiterole_delete(
                invitation_id=invitation_id, site_id=site_id, role_id=role_id)

        return result

    # invitationsiterole_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:invitationsiterole", "read")])
    async def invitationsiterole_read(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            invitation_site_role = await request.app["access_control_api"].invitationsiterole_read(
                invitation_id=invitation_id, site_id=site_id, role_id=role_id)

        if invitation_site_role:
            transform = transformations.INVITATION_SITE_ROLE
            result = transform.apply(invitation_site_role.to_dict())
            return result

        return None

    # get_all_user_roles -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:site", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:siterole", "read"),
                               ("urn:ge:access_control:userdomainrole", "read"),
                               ("urn:ge:access_control:usersiterole", "read"),
                               ], target_user_field=1)
    async def get_all_user_roles(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user_roles = await request.app["operational_api"].get_all_user_roles(user_id)
            return user_roles.to_dict()

    # get_domain_roles -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:domainrole", "read")])
    async def get_domain_roles(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain_roles = await request.app["operational_api"].get_domain_roles(domain_id)
            return domain_roles.to_dict()

    # get_site_from_client_token_id -- Synchronisation point for meld
    @staticmethod
    # The permission is checked in the function and not via a decorator.
    async def get_site_from_client_token_id(request, client_token_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_token_id: string A client token id. This is not the primary key of the client table, but rather the client id that is typically configured along with the client secret.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        # In order to be allowed to request the site info for a particular client ID, the client ID
        # needs to be the audience of the JWT token used to make the request.
        if request["token"]["aud"] != client_token_id:
            raise JSONForbidden(message="Token client id must match the one used in the API call")

        nocache = kwargs.get("nocache", False)
        if nocache:
            # When nocache is set, we perform all the lookups via the API.
            with client_exception_handler():
                try:
                    [client] = await request.app["authentication_service_api"].client_list(
                        client_token_id=client_token_id)
                    [site] = await request.app["access_control_api"].site_list(client_id=client.id)
                    transform = transformations.SITE
                    result = transform.apply(site.to_dict())
                except Exception as e:
                    raise JSONNotFound(message=str(e))
        else:
            try:
                site_id = mappings.Mappings.site_id_for(client_token_id)
                result = mappings.Mappings.site_by_id(site_id)
            except KeyError as e:
                raise JSONNotFound(message=str(e))

        return result

    # get_sites_under_domain -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:site", "read")],
                         allow_for_management_portal=True)
    async def get_sites_under_domain(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            sites = await request.app["operational_api"].get_sites_under_domain(domain_id)
            transform = transformations.SITE
            return [transform.apply(site.to_dict()) for site in sites]

    # get_site_and_domain_roles -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:site", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:siterole", "read")])
    async def get_site_and_domain_roles(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_and_domain_roles = await request.app["operational_api"].get_site_and_domain_roles(site_id)
            return site_and_domain_roles.to_dict()

    # get_site_role_labels_aggregated -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:site", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:siterole", "read")])
    async def get_site_role_labels_aggregated(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_role_labels_aggregated = await request.app["operational_api"].get_site_role_labels_aggregated(site_id)
            return site_role_labels_aggregated.to_dict()

    # get_user_domain_permissions -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "read"),
                               ("urn:ge:access_control:resource", "read"),
                               ("urn:ge:access_control:roleresourcepermission", "read"),
                               ], target_user_field=1)
    async def get_user_domain_permissions(request, user_id, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        result = []

        try:
            user = uuid.UUID(user_id)
        except ValueError:
            raise JSONBadRequest(message="Malformed user id")

        nocache = kwargs.get("nocache", False)
        roles_for_domain = await utils.get_user_roles_for_domain(request, user, domain_id,
                                                                 nocache=nocache)
        if roles_for_domain:
            tech_admin_role_id = mappings.Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)

            if tech_admin_role_id in roles_for_domain:
                result = mappings.Mappings.all_resource_permissions()
                # There is also an API call that can be used, if necessary:
                # resource_permissions = await request.app[
                #     "operational_api"].get_tech_admin_resource_permissions()
            else:
                with client_exception_handler():
                    resource_permissions = await request.app[
                        "operational_api"].get_resource_permissions_for_roles(
                            role_ids=list(roles_for_domain))

                # Resource permissions are presented as a concatenation of the resource URN, a semicolon
                # and the permission name. The API calls above return identifiers, so we need to map it.
                result = [
                    "{}:{}".format(mappings.Mappings.resource_urn_for(rp.resource_id),
                                   mappings.Mappings.permission_name_for(rp.permission_id))
                    for rp in resource_permissions
                ]

        return result

    # user_has_permissions -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:site", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:siterole", "read"),
                               ("urn:ge:access_control:userdomainrole", "read"),
                               ("urn:ge:access_control:usersiterole", "read"),
                               ("urn:ge:access_control:permission", "read"),
                               ("urn:ge:access_control:resource", "read"),
                               ], target_user_field=2)
    async def user_has_permissions(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        # The request body uses strings to identify resources and permissions.
        # We convert it to their integer representations here as a validation step.
        try:
            resource_permissions = [
                (mappings.Mappings.resource_id_for(item["resource"]),
                 mappings.Mappings.permission_id_for(item["permission"]))
                for item in body["resource_permissions"]
            ]
        except KeyError as e:
            raise JSONBadRequest(message=str(e))

        nocache = body.get("nocache", False)
        operator_string = body["operator"]
        if operator_string == "any":
            operator = any
        elif operator_string == "all":
            operator = all
        else:
            raise JSONBadRequest(message=f"Invalid operator specified: {operator_string}.")

        site_id = body.get("site_id")
        domain_id = body.get("domain_id")

        # Either a site_id or domain_id needs to be specified.
        if site_id is None and domain_id is None or \
           site_id is not None and domain_id is not None:
            raise JSONBadRequest(message="Either site_id or domain_id needs to be specified")

        result = await utils.user_has_permissions(request, user_id, operator, resource_permissions,
                                                  site=site_id, domain=domain_id, nocache=nocache)
        return {"has_permissions": result}

    # get_user_management_portal_permissions -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "read"),
                               ("urn:ge:access_control:resource", "read"),
                               ("urn:ge:access_control:roleresourcepermission", "read"),
                               ], target_user_field=1)
    async def get_user_management_portal_permissions(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        if request["token"]["aud"] != MANAGEMENT_PORTAL_CLIENT_ID:
            raise JSONForbidden(message="Only the Management Portal can use this API call")

        try:
            user = uuid.UUID(user_id)
        except ValueError:
            raise JSONBadRequest(message="Malformed user id")

        try:
            management_portal_site_id = mappings.Mappings.site_id_for(MANAGEMENT_PORTAL_CLIENT_ID)
        except KeyError:
            raise JSONBadRequest(message="Misconfigured Management Portal Client ID")

        nocache = kwargs.get("nocache", False)
        roles = await utils.get_user_roles_for_site(request, user, management_portal_site_id,
                                                    nocache=nocache)

        if not roles:
            # No roles are linked to the user for the Management Portal
            return []

        tech_admin_role_id = mappings.Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)

        if tech_admin_role_id in roles:
            result = mappings.Mappings.all_resource_permissions()
            # There is also an API call that can be used, if necessary:
            # resource_permissions = await request.app[
            #     "operational_api"].get_tech_admin_resource_permissions()
        else:
            with client_exception_handler():
                resource_permissions = await request.app[
                    "operational_api"].get_resource_permissions_for_roles(role_ids=list(roles))

                # Resource permissions are presented as a concatenation of the resource URN, a semicolon
                # and the permission name. The API calls above return identifiers, so we need to map it.
                result = [
                    "{}:{}".format(mappings.Mappings.resource_urn_for(rp.resource_id),
                                   mappings.Mappings.permission_name_for(rp.permission_id))
                    for rp in resource_permissions
                ]

        return result

    # get_user_site_permissions -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "read"),
                               ("urn:ge:access_control:resource", "read"),
                               ("urn:ge:access_control:roleresourcepermission", "read"),
                               ], target_user_field=1)
    async def get_user_site_permissions(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        result = []

        try:
            user = uuid.UUID(user_id)
        except ValueError:
            raise JSONBadRequest(message="Malformed user id")

        nocache = kwargs.get("nocache", False)
        roles_for_site = await utils.get_user_roles_for_site(request, user, site_id,
                                                             nocache=nocache)
        if roles_for_site:
            tech_admin_role_id = mappings.Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)

            if tech_admin_role_id in roles_for_site:
                result = mappings.Mappings.all_resource_permissions()
                # There is also an API call that can be used, if necessary:
                # resource_permissions = await request.app[
                #     "operational_api"].get_tech_admin_resource_permissions()
            else:
                with client_exception_handler():
                    resource_permissions = await request.app[
                        "operational_api"].get_resource_permissions_for_roles(
                            role_ids=list(roles_for_site))

                # Resource permissions are presented as a concatenation of the resource URN, a semicolon
                # and the permission name. The API calls above return identifiers, so we need to map it.
                result = [
                    "{}:{}".format(mappings.Mappings.resource_urn_for(rp.resource_id),
                                   mappings.Mappings.permission_name_for(rp.permission_id))
                    for rp in resource_permissions
                ]

        return result

    # get_user_site_role_labels_aggregated -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:site", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:siterole", "read"),
                               ("urn:ge:access_control:userdomainrole", "read"),
                               ("urn:ge:access_control:usersiterole", "read"),
                               ], target_user_field=1)
    async def get_user_site_role_labels_aggregated(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user_site_role_labels_aggregated = await request.app["operational_api"].get_user_site_role_labels_aggregated(user_id, site_id)
            return user_site_role_labels_aggregated.to_dict()

    # get_users_with_roles_for_domain -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:userdomainrole", "read")])
    async def get_users_with_roles_for_domain(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            # Get access control response.
            response = await request.app["operational_api"].get_users_with_roles_for_domain(domain_id)
        return await transform_users_with_roles(request, response, **kwargs)

    # get_users_with_roles_for_site -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read"),
                               ("urn:ge:access_control:domainrole", "read"),
                               ("urn:ge:access_control:userdomainrole", "read"),
                               ("urn:ge:access_control:site", "read"),
                               ("urn:ge:access_control:siterole", "read"),
                               ("urn:ge:access_control:usersiterole", "read")])
    async def get_users_with_roles_for_site(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            # Get access control response.
            response = await request.app["operational_api"].get_users_with_roles_for_site(site_id)
        return await transform_users_with_roles(request, response, **kwargs)

    # organisation_list -- Synchronisation point for meld
    @staticmethod
    # No permissions are required for this
    async def organisation_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param organisation_ids (optional): array An optional list of organisation ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            organisations, _status, headers = await request.app[
                "authentication_service_api"].organisation_list_with_http_info(**kwargs)

        if organisations:
            transform = transformations.ORGANISATION
            organisations = [transform.apply(organisation.to_dict())
                             for organisation in organisations]

        return organisations, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # organisation_create -- Synchronisation point for meld
    @staticmethod
    async def organisation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            organisation = await request.app["authentication_service_api"].organisation_create(
                organisation_create=body)

        if organisation:
            transform = transformations.ORGANISATION
            result = transform.apply(organisation.to_dict())
            return result

        return None

    # organisation_delete -- Synchronisation point for meld
    @staticmethod
    async def organisation_delete(request, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param organisation_id: integer An integer identifying an organisation
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["authentication_service_api"].organisation_delete(
                organisation_id)

        return result

    # organisation_read -- Synchronisation point for meld
    @staticmethod
    # No permissions are required for this
    async def organisation_read(request, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param organisation_id: integer An integer identifying an organisation
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            organisation = await request.app["authentication_service_api"].organisation_read(
                organisation_id)

        if organisation:
            transform = transformations.ORGANISATION
            result = transform.apply(organisation.to_dict())
            return result

        return None

    # organisation_update -- Synchronisation point for meld
    @staticmethod
    async def organisation_update(request, body, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param organisation_id: integer An integer identifying an organisation
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            organisation = await request.app["authentication_service_api"].organisation_update(
                organisation_id=organisation_id,
                organisation_update=body
            )

        if organisation:
            transform = transformations.ORGANISATION
            result = transform.apply(organisation.to_dict())
            return result

        return None

    # permission_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "read")])
    async def permission_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param permission_ids (optional): array An optional list of permission ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            permissions, _status, headers = await request.app[
                "access_control_api"].permission_list_with_http_info(**kwargs)

        if permissions:
            transform = transformations.PERMISSION
            permissions = [transform.apply(permission.to_dict()) for permission in permissions]

        return permissions, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # permission_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "create")])
    async def permission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            permission = await request.app["access_control_api"].permission_create(
                permission_create=body)

        if permission:
            transform = transformations.PERMISSION
            result = transform.apply(permission.to_dict())
            return result

        return None

    # permission_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "delete")])
    async def permission_delete(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].permission_delete(permission_id)

        return result

    # permission_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "read")])
    async def permission_read(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            permission = await request.app["access_control_api"].permission_read(permission_id)

        if permission:
            transform = transformations.PERMISSION
            result = transform.apply(permission.to_dict())
            return result

        return None

    # permission_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:permission", "update")])
    async def permission_update(request, body, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            permission = await request.app["access_control_api"].permission_update(permission_id,
                                                                                   permission_update=body)

        if permission:
            transform = transformations.PERMISSION
            result = transform.apply(permission.to_dict())
            return result

        return None

    # refresh_all -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def refresh_all(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_all(request.app, **kwargs)
        return {}

    # refresh_clients -- Synchronisation point for meld
    @staticmethod
    async def refresh_clients(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_clients(request.app, **kwargs)
        return {}

    # refresh_domains -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def refresh_domains(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_domains(request.app, **kwargs)
        return {}

    # refresh_keys -- Synchronisation point for meld
    @staticmethod
    async def refresh_keys(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_keys(request.app, **kwargs)
        return {}

    # refresh_permissions -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def refresh_permissions(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_permissions(request.app, **kwargs)
        return {}

    # refresh_resources -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def refresh_resources(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_resources(request.app, **kwargs)
        return {}

    # refresh_roles -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def refresh_roles(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_roles(request.app, **kwargs)
        return {}

    # refresh_sites -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def refresh_sites(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        await mappings.refresh_sites(request.app, **kwargs)
        return {}

    # request_user_deletion -- Synchronisation point for meld
    @staticmethod
    @require_permissions(any, [])  # Tech admin only
    async def request_user_deletion(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        # The caller of this function is considered the deleter.
        body["deleter_id"] = request["token"]["sub"]

        with client_exception_handler():
            result = await request.app["authentication_service_api"].request_user_deletion(
                request_user_deletion=body)

        return result

    # resource_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:resource", "read")])
    async def resource_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param prefix (optional): string An optional URN prefix filter
        :param resource_ids (optional): array An optional list of resource ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            resources, _status, headers = await request.app[
                "access_control_api"].resource_list_with_http_info(**kwargs)

        if resources:
            transform = transformations.RESOURCE
            resources = [transform.apply(resource.to_dict()) for resource in resources]

        return resources, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # resource_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:resource", "create")])
    async def resource_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            resource = await request.app["access_control_api"].resource_create(resource_create=body)

        if resource:
            transform = transformations.RESOURCE
            result = transform.apply(resource.to_dict())
            return result

        return None

    # resource_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:resource", "delete")])
    async def resource_delete(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].resource_delete(resource_id)

        return result

    # resource_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:resource", "read")])
    async def resource_read(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            resource = await request.app["access_control_api"].resource_read(resource_id)

        if resource:
            transform = transformations.RESOURCE
            result = transform.apply(resource.to_dict())
            return result

        return None

    # resource_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:resource", "update")])
    async def resource_update(request, body, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            resource = await request.app["access_control_api"].resource_update(resource_id,
                                                                               resource_update=body)

        if resource:
            transform = transformations.RESOURCE
            result = transform.apply(resource.to_dict())
            return result

        return None

    # roleresourcepermission_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:roleresourcepermission", "read")])
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
        with client_exception_handler():
            rrps, _status, headers = await request.app[
                "access_control_api"].roleresourcepermission_list_with_http_info(**kwargs)

        if rrps:
            transform = transformations.ROLE_RESOURCE_PERMISSION
            rrps = [transform.apply(rrp.to_dict()) for rrp in rrps]

        return rrps, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # roleresourcepermission_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:roleresourcepermission", "create")])
    async def roleresourcepermission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            rrp = await request.app["access_control_api"].roleresourcepermission_create(
                role_resource_permission_create=body)

        if rrp:
            transform = transformations.ROLE_RESOURCE_PERMISSION
            result = transform.apply(rrp.to_dict())
            return result

        return None

    # roleresourcepermission_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:roleresourcepermission", "delete")])
    async def roleresourcepermission_delete(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].access_control_roleresourcepermission_delete(
                role_id, resource_id, permission_id)

        return result

    # roleresourcepermission_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:roleresourcepermission", "read")])
    async def roleresourcepermission_read(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            rrp = await request.app["access_control_api"].roleresourcepermission_read(role_id, resource_id, permission_id)

        if rrp:
            transform = transformations.ROLE_RESOURCE_PERMISSION
            result = transform.apply(rrp.to_dict())
            return result

        return None

    # role_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:role", "read")])
    async def role_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_ids (optional): array An optional list of role ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            roles, _status, headers = await request.app[
                "access_control_api"].role_list_with_http_info(**kwargs)

        if roles:
            transform = transformations.ROLE
            roles = [transform.apply(role.to_dict()) for role in roles]

        return roles, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # role_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:role", "create")])
    async def role_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            role = await request.app["access_control_api"].role_create(role_create=body)

        if role:
            transform = transformations.ROLE
            result = transform.apply(role.to_dict())
            return result

        return None

    # role_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:role", "delete")])
    async def role_delete(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].role_delete(role_id)

        return result

    # role_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:role", "read")])
    async def role_read(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            role = await request.app["access_control_api"].role_read(role_id)

        if role:
            transform = transformations.ROLE
            result = transform.apply(role.to_dict())
            return result

        return None

    # role_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:role", "update")])
    async def role_update(request, body, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            role = await request.app["access_control_api"].role_update(role_id, role_update=body)

        if role:
            transform = transformations.ROLE
            result = transform.apply(role.to_dict())
            return result

        return None

    # sitedataschema_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:sitedataschema", "read")])
    async def sitedataschema_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            sdss, _status, headers = await request.app[
                "user_data_api"].sitedataschema_list_with_http_info(**kwargs)

        if sdss:
            transform = transformations.SITE_DATA_SCHEMA
            sdss = [transform.apply(sds.to_dict()) for sds in sdss]

        return sdss, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # sitedataschema_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:sitedataschema", "create")])
    async def sitedataschema_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            sds = await request.app["user_data_api"].sitedataschema_create(
                site_data_schema_create=body)

        if sds:
            transform = transformations.SITE_DATA_SCHEMA
            result = transform.apply(sds.to_dict())
            return result

        return None

    # sitedataschema_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:sitedataschema", "delete")])
    async def sitedataschema_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["user_data_api"].sitedataschema_delete(site_id)

        return result

    # sitedataschema_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:sitedataschema", "read")])
    async def sitedataschema_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            sds = await request.app["user_data_api"].sitedataschema_read(site_id)

        if sds:
            transform = transformations.SITE_DATA_SCHEMA
            result = transform.apply(sds.to_dict())
            return result

        return None

    # sitedataschema_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:sitedataschema", "update")])
    async def sitedataschema_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            sds = await request.app["user_data_api"].sitedataschema_update(
                site_id, site_data_schema_update=body)

        if sds:
            transform = transformations.SITE_DATA_SCHEMA
            result = transform.apply(sds.to_dict())
            return result

        return None

    # siterole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:siterole", "read")])
    async def siterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_roles, _status, headers = await request.app[
                "access_control_api"].siterole_list_with_http_info(**kwargs)

        if site_roles:
            transform = transformations.SITE_ROLE
            site_roles = [transform.apply(site_role.to_dict()) for site_role in site_roles]

        return site_roles, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # siterole_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:siterole", "create")])
    async def siterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_role = await request.app["access_control_api"].siterole_create(
                site_role_create=body)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    # siterole_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:siterole", "delete")])
    async def siterole_delete(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].siterole_delete(site_id, role_id)

        return result

    # siterole_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:siterole", "read")])
    async def siterole_read(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_role = await request.app["access_control_api"].siterole_read(site_id, role_id)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    # siterole_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:siterole", "update")])
    async def siterole_update(request, body, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_role = await request.app["access_control_api"].siterole_update(
                site_id, role_id, site_role_update=body)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    # site_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:site", "read")],
                         allow_for_management_portal=True)
    async def site_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        :param client_id (optional): integer An optional client id to filter on
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            sites, _status, headers = await request.app[
                "access_control_api"].site_list_with_http_info(**kwargs)

        if sites:
            transform = transformations.SITE
            sites = [transform.apply(site.to_dict()) for site in sites]

        return sites, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # site_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:site", "create")])
    async def site_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site = await request.app["access_control_api"].site_create(site_create=body)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    # site_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:site", "delete")])
    async def site_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].site_delete(site_id)

        return result

    # site_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:site", "read")],
                         allow_for_management_portal=True)
    async def site_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site = await request.app["access_control_api"].site_read(site_id)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    # site_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:site", "update")])
    async def site_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site = await request.app["access_control_api"].site_update(site_id, site_update=body)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    # userdomainrole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:userdomainrole", "read")],
                         target_user_field="user_id")
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
        with client_exception_handler():
            udrs, _status, headers = await request.app[
                "access_control_api"].userdomainrole_list_with_http_info(**kwargs)

        if udrs:
            transform = transformations.USER_DOMAIN_ROLE
            udrs = [transform.apply(udr.to_dict()) for udr in udrs]

        return udrs, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # userdomainrole_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:userdomainrole", "create")])
    @requester_has_role(body_field=1)
    async def userdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user = await request.app["authentication_service_api"].user_read(user_id=body[
                "user_id"])

            if not user:
                raise JSONForbidden(message="The target user does not exist")

            if user.organisation_id is None:
                raise JSONForbidden(message="The target user is not linked to an organisation")

            user_domain_role = await request.app["access_control_api"].userdomainrole_create(
                user_domain_role_create=body)

        if user_domain_role:
            transform = transformations.USER_DOMAIN_ROLE
            result = transform.apply(user_domain_role.to_dict())
            return result

        return None

    # userdomainrole_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:userdomainrole", "delete")])
    @requester_has_role(target_user_id_field=1, domain_id_field=2, role_id_field=3)
    async def userdomainrole_delete(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].userdomainrole_delete(user_id, domain_id, role_id)

        return result

    # userdomainrole_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:userdomainrole", "read")],
                         target_user_field=1)
    async def userdomainrole_read(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            udr = await request.app["access_control_api"].userdomainrole_read(user_id, domain_id, role_id)

        if udr:
            transform = transformations.USER_DOMAIN_ROLE
            result = transform.apply(udr.to_dict())
            return result

        return None

    # user_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:identity_provider:user", "read")])
    async def user_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param birth_date (optional): string An optional birth_date range filter
        :param country (optional): string An optional country filter
        :param date_joined (optional): string An optional date joined range filter
        :param email (optional): string An optional case insensitive email inner match filter
        :param email_verified (optional): boolean An optional email verified filter
        :param first_name (optional): string An optional case insensitive first name inner match filter
        :param gender (optional): string An optional gender filter
        :param is_active (optional): boolean An optional is_active filter
        :param last_login (optional): string An optional last login range filter
        :param last_name (optional): string An optional case insensitive last name inner match filter
        :param msisdn (optional): string An optional case insensitive MSISDN inner match filter
        :param msisdn_verified (optional): boolean An optional MSISDN verified filter
        :param nickname (optional): string An optional case insensitive nickname inner match filter
        :param organisation_id (optional): integer An optional filter on the organisation id
        :param updated_at (optional): string An optional updated_at range filter
        :param username (optional): string An optional case insensitive username inner match filter
        :param q (optional): string An optional case insensitive inner match filter across all searchable text fields
        :param tfa_enabled (optional): boolean An optional filter based on whether a user has 2FA enabled or not
        :param has_organisation (optional): boolean An optional filter based on whether a user belongs to an organisation or not
        :param order_by (optional): array Fields and directions to order by, e.g. "-created_at,username". Add "-" in front of a field name to indicate descending order.
        :param user_ids (optional): array An optional list of user ids
        :param site_ids (optional): array An optional list of site ids
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            users, _status, headers = await request.app[
                "authentication_service_api"].user_list_with_http_info(**kwargs)

        if users:
            transform = transformations.USER
            users = [transform.apply(user.to_dict()) for user in users]

        return users, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # user_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:identity_provider:user", "delete")])
    async def user_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["authentication_service_api"].user_delete(user_id)

        return result

    # user_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:identity_provider:user", "read")], target_user_field=1)
    async def user_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user = await request.app["authentication_service_api"].user_read(user_id)

        if user:
            transform = transformations.USER
            result = transform.apply(user.to_dict())
            return result

        return None

    # user_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:identity_provider:user", "update")], target_user_field=2)
    async def user_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user = await request.app["authentication_service_api"].user_update(user_id,
                                                                               user_update=body)

        if user:
            transform = transformations.USER
            result = transform.apply(user.to_dict())
            return result

        return None

    # usersitedata_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "read")],
                         target_user_field="user_id")
    async def usersitedata_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usds, _status, headers = await request.app[
                "user_data_api"].usersitedata_list_with_http_info(**kwargs)

        if usds:
            transform = transformations.USER_SITE_DATA
            usds = [transform.apply(usd.to_dict()) for usd in usds]

        return usds, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # usersitedata_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "create")])
    # The targeted user should not be allowed to make this call. This is admin only.
    async def usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usd = await request.app["user_data_api"].usersitedata_create(user_site_data_create=body)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

        return None

    # usersitedata_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "delete")])
    # The targeted user should not be allowed to make this call. This is admin only.
    async def usersitedata_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["user_data_api"].usersitedata_delete(user_id, site_id)

        return result

    # usersitedata_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "read")], target_user_field=1)
    async def usersitedata_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usd = await request.app["user_data_api"].usersitedata_read(user_id, site_id)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

        return None

    # usersitedata_update -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "update")])
    # The targeted user should not be allowed to make this call. This is admin only.
    async def usersitedata_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usd = await request.app["user_data_api"].usersitedata_update(user_id, site_id,
                                                                         user_site_data_update=body)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

    # usersiterole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:usersiterole", "read")],
                         target_user_field="user_id")
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
        with client_exception_handler():
            usrs, _status, headers = await request.app[
                "access_control_api"].usersiterole_list_with_http_info(**kwargs)

        if usrs:
            transform = transformations.USER_SITE_ROLE
            usrs = [transform.apply(usr.to_dict()) for usr in usrs]

        return usrs, {
            TOTAL_COUNT_HEADER: headers.get(CLIENT_TOTAL_COUNT_HEADER, "0")
        }

    # usersiterole_create -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:usersiterole", "create")])
    @requester_has_role(body_field=1)
    async def usersiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user = await request.app["authentication_service_api"].user_read(user_id=body[
                "user_id"])

            if not user:
                raise JSONForbidden(message="The target user does not exist")

            if user.organisation_id is None:
                raise JSONForbidden(message="The target user is not linked to an organisation")

            user_site_role = await request.app["access_control_api"].usersiterole_create(
                user_site_role_create=body)

        if user_site_role:
            transform = transformations.USER_SITE_ROLE
            result = transform.apply(user_site_role.to_dict())
            return result

        return None

    # usersiterole_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:usersiterole", "delete")])
    @requester_has_role(target_user_id_field=1, site_id_field=2, role_id_field=3)
    async def usersiterole_delete(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            result = await request.app["access_control_api"].usersiterole_delete(user_id, site_id, role_id)

        return result

    # usersiterole_read -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:usersiterole", "read")], target_user_field=1)
    async def usersiterole_read(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usr = await request.app["access_control_api"].usersiterole_read(user_id, site_id, role_id)

        if usr:
            transform = transformations.USER_SITE_ROLE
            result = transform.apply(usr.to_dict())
            return result

        return None
