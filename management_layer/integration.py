from management_layer.api.stubs import AbstractStubClass
from management_layer.configuration import access_control_api, user_data_api, authentication_api
from management_layer.transformation import Transformation, Mapping
from management_layer import transformations
from management_layer.utils import client_exception_handler

# API clients generated from the Swagger specifications of the
# respective components.

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
    async def adminnote_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param creator_id (optional): string An optional query parameter to filter by creator (a user_id)
        """
        transform = Transformation(
            mappings=[
               Mapping("offset", conversion=int),
               Mapping("limit", conversion=int),
            ],
            copy_fields=["user_id", "creator_id"]
        )
        with client_exception_handler():
            admin_notes = await user_data_api.adminnote_list(**transform.apply(kwargs))

        if admin_notes:
            transform = transformations.ADMIN_NOTE
            result = [transform.apply(note.to_dict()) for note in admin_notes]
            return result

        return []

    @staticmethod
    async def adminnote_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            admin_note = await user_data_api.adminnote_create(data=body)

        if admin_note:
            transform = transformations.ADMIN_NOTE
            return transform.apply(admin_note.to_dict())

        return None

    @staticmethod
    async def adminnote_delete(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        """
        with client_exception_handler():
            result = await user_data_api.adminnote_delete(admin_note_id)

        return result

    @staticmethod
    async def adminnote_read(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        """
        with client_exception_handler():
            admin_note = await user_data_api.adminnote_read(admin_note_id)

        if admin_note:
            transform = transformations.ADMIN_NOTE
            return transform.apply(admin_note.to_dict())

        return None

    @staticmethod
    async def adminnote_update(request, body, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param admin_note_id: integer A unique integer value identifying the admin note.
        """
        with client_exception_handler():
            admin_note = await user_data_api.adminnote_update(admin_note_id, data=body)

        if admin_note:
            transform = transformations.ADMIN_NOTE
            return transform.apply(admin_note.to_dict())

        return None

    @staticmethod
    async def client_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param client_ids (optional): array An optional list of client ids
        """
        raise NotImplementedError()

    @staticmethod
    async def client_read(request, client_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_id: string A UUID value identifying the client
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
        """
        # All optional args are integers:
        kwargs = {k: int(v) for k, v in kwargs.items()}
        with client_exception_handler():
            domain_roles = await access_control_api.domainrole_list(**kwargs)

        if domain_roles:
            transform = transformations.DOMAIN_ROLE
            result = [transform.apply(domain_role.to_dict()) for domain_role in domain_roles]
            return result

        return []

    @staticmethod
    async def domainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            domain_role = await access_control_api.domainrole_create(data=body)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    @staticmethod
    async def domainrole_delete(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            result = await access_control_api.domainrole_delete(domain_id, role_id)

        return result

    @staticmethod
    async def domainrole_read(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            domain_role = await access_control_api.domainrole_read(domain_id, role_id)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    @staticmethod
    async def domainrole_update(request, body, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            domain_role = await access_control_api.domainrole_update(domain_id, role_id, data=body)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    @staticmethod
    async def domain_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param domain_ids (optional): array An optional list of domain ids
        """
        kwargs = {k: int(v) for k, v in kwargs.items()}
        with client_exception_handler():
            domains = await access_control_api.domain_list(**kwargs)

        if domains:
            transform = transformations.DOMAIN
            result = [transform.apply(domain.to_dict()) for domain in domains]
            return result

        return []

    @staticmethod
    async def domain_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            domain = await access_control_api.domain_create(data=body)

        if domain:
            transform = transformations.DOMAIN
            result = transform.apply(domain.to_dict())
            return result

        return None

    @staticmethod
    async def domain_delete(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        with client_exception_handler():
            result = await access_control_api.domain_delete(domain_id)

        return result

    @staticmethod
    async def domain_read(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        with client_exception_handler():
            domain = await access_control_api.domain_read(domain_id)

        if domain:
            transform = transformations.DOMAIN
            result = transform.apply(domain.to_dict())
            return result

        return None

    @staticmethod
    async def domain_update(request, body, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        """
        with client_exception_handler():
            domain = await access_control_api.domain_update(domain_id, data=body)

        if domain:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain.to_dict())
            return result

        return None

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
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_delete(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationdomainrole_read(request, invitation_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
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
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_delete(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_read(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitation_update(request, body, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitation_id: string A UUID value identifying the invitation.
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
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_delete(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def invitationsiterole_read(request, invitation_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_all_user_roles(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_domain_roles(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_site_and_domain_roles(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_site_role_labels_aggregated(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get_user_site_role_labels_aggregated(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def permission_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param permission_ids (optional): array An optional list of permission ids
        """
        kwargs = {k: int(v) for k, v in kwargs.items()}
        with client_exception_handler():
            permissions = await access_control_api.permission_list(**kwargs)

        if permissions:
            transform = transformations.PERMISSION
            result = [transform.apply(permission.to_dict()) for permission in permissions]
            return result

        return []

    @staticmethod
    async def permission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            permission = await access_control_api.permission_create(data=body)

        if permission:
            transform = transformations.PERMISSION
            result = transform.apply(permission.to_dict())
            return result

        return None

    @staticmethod
    async def permission_delete(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        """
        with client_exception_handler():
            result = await access_control_api.permission_delete(permission_id)

        return result

    @staticmethod
    async def permission_read(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        """
        with client_exception_handler():
            permission = await access_control_api.permission_read(permission_id)

        if permission:
            transform = transformations.PERMISSION
            result = transform.apply(permission.to_dict())
            return result

        return None

    @staticmethod
    async def permission_update(request, body, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param permission_id: integer A unique integer value identifying the permission.
        """
        with client_exception_handler():
            permission = await access_control_api.permission_update(permission_id, data=body)

        if permission:
            transform = transformations.PERMISSION
            result = transform.apply(permission.to_dict())
            return result

        return None

    @staticmethod
    async def resource_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param prefix (optional): string An optional URN prefix filter
        :param resource_ids (optional): array An optional list of resource ids
        """
        if "offset" in kwargs:
            kwargs["offset"] = int(kwargs["offset"])
        if "limit" in kwargs:
            kwargs["limit"] = int(kwargs["limit"])
        if "resource_ids" in kwargs:
            kwargs["resource_ids"] = [int(rid) for rid in kwargs["resource_ids"]]

        with client_exception_handler():
            resources = await access_control_api.resource_list(**kwargs)

        if resources:
            transform = transformations.RESOURCE
            result = [transform.apply(resource.to_dict()) for resource in resources]
            return result

        return []

    @staticmethod
    async def resource_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            resource = access_control_api.resource_create(data=body)

        if resource:
            transform = transformations.RESOURCE
            result = transform.apply(resource.to_dict())
            return result

        return None

    @staticmethod
    async def resource_delete(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        """
        with client_exception_handler():
            result = access_control_api.resource_delete(resource_id)

        return result

    @staticmethod
    async def resource_read(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        """
        with client_exception_handler():
            resource = access_control_api.resource_read(resource_id)

        if resource:
            transform = transformations.RESOURCE
            result = transform.apply(resource.to_dict())
            return result

        return None

    @staticmethod
    async def resource_update(request, body, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param resource_id: integer A unique integer value identifying the resource.
        """
        with client_exception_handler():
            resource = access_control_api.resource_update(resource_id, data=body)

        if resource:
            transform = transformations.RESOURCE
            result = transform.apply(resource.to_dict())
            return result

        return None

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
        # All optional parameters are integers
        kwargs = {k: int(v) for k, v in kwargs.items()}
        with client_exception_handler():
            rrps = access_control_api.roleresourcepermission_list(**kwargs)

        if rrps:
            transform = transformations.ROLE_RESOURCE_PERMISSION
            result = [transform.apply(rrp.to_dict()) for rrp in rrps]
            return result

        return []

    @staticmethod
    async def roleresourcepermission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            rrp = access_control_api.roleresourcepermission_create(data=body)

        if rrp:
            transform = transformations.ROLE_RESOURCE_PERMISSION
            result = transform.apply(rrp.to_dict())
            return result

        return None

    @staticmethod
    async def roleresourcepermission_delete(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        """
        with client_exception_handler():
            result = access_control_api.access_control_roleresourcepermission_delete(
                role_id, resource_id, permission_id)

        return result

    @staticmethod
    async def roleresourcepermission_read(request, role_id, resource_id, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :param resource_id: integer A unique integer value identifying the resource.
        :param permission_id: integer A unique integer value identifying the permission.
        """
        with client_exception_handler():
            rrp = access_control_api.roleresourcepermission_read(role_id, resource_id, permission_id)

        if rrp:
            transform = transformations.ROLE_RESOURCE_PERMISSION
            result = transform.apply(rrp.to_dict())
            return result

        return None

    @staticmethod
    async def role_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param role_ids (optional): array An optional list of role ids
        """
        if "offset" in kwargs:
            kwargs["offset"] = int(kwargs["offset"])
        if "limit" in kwargs:
            kwargs["limit"] = int(kwargs["limit"])
        if "role_ids" in kwargs:
            kwargs["role_ids"] = [int(role_id) for role_id in kwargs["role_ids"]]

        with client_exception_handler():
            roles = access_control_api.role_list(**kwargs)

        if roles:
            transform = transformations.ROLE
            result = [transform.apply(role.to_dict()) for role in roles]
            return result

        return []

    @staticmethod
    async def role_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            role = access_control_api.role_create(data=body)

        if role:
            transform = transformations.ROLE
            result = transform.apply(role.to_dict())
            return result

        return None

    @staticmethod
    async def role_delete(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            result = access_control_api.role_delete(role_id)

        return result

    @staticmethod
    async def role_read(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            role = access_control_api.role_read(role_id)

        if role:
            transform = transformations.ROLE
            result = transform.apply(role.to_dict())
            return result

        return None

    @staticmethod
    async def role_update(request, body, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            role = access_control_api.role_update(role_id, data=body)

        if role:
            transform = transformations.ROLE
            result = transform.apply(role.to_dict())
            return result

        return None

    @staticmethod
    async def sitedataschema_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        """
        if "offset" in kwargs:
            kwargs["offset"] = int(kwargs["offset"])
        if "limit" in kwargs:
            kwargs["limit"] = int(kwargs["limit"])
        if "site_ids" in kwargs:
            kwargs["site_ids"] = [int(site_id) for site_id in kwargs["site_ids"]]

        with client_exception_handler():
            sdss = user_data_api.sitedataschema_list(**kwargs)

        if sdss:
            transform = transformations.SITE_DATA_SCHEMA
            result = [transform.apply(sds.to_dict()) for sds in sdss]
            return result

        return []

    @staticmethod
    async def sitedataschema_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            sds = user_data_api.sitedataschema_create(data=body)

        if sds:
            transform = transformations.SITE_DATA_SCHEMA
            result = transform.apply(sds.to_dict())
            return result

        return None

    @staticmethod
    async def sitedataschema_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            result = user_data_api.sitedataschema_delete(site_id)

        return result

    @staticmethod
    async def sitedataschema_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            sds = user_data_api.sitedataschema_read(site_id)

        if sds:
            transform = transformations.SITE_DATA_SCHEMA
            result = transform.apply(sds.to_dict())
            return result

        return None

    @staticmethod
    async def sitedataschema_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            sds = user_data_api.sitedataschema_update(site_id, data=body)

        if sds:
            transform = transformations.SITE_DATA_SCHEMA
            result = transform.apply(sds.to_dict())
            return result

        return None

    @staticmethod
    async def siterole_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :param role_id (optional): integer An optional query parameter to filter by role_id
        """
        # All optional params are integers
        kwargs = {k: int(v) for k, v in kwargs}
        with client_exception_handler():
            site_roles = access_control_api.siterole_list(**kwargs)

        if site_roles:
            transform = transformations.SITE_ROLE
            result = [transform.apply(site_role.to_dict()) for site_role in site_roles]
            return result

        return []

    @staticmethod
    async def siterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            site_role = access_control_api.siterole_create(data=body)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    @staticmethod
    async def siterole_delete(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            result = access_control_api.siterole_delete(site_id, role_id)

        return result

    @staticmethod
    async def siterole_read(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            site_role = access_control_api.siterole_read(site_id, role_id)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    @staticmethod
    async def siterole_update(request, body, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            site_role = access_control_api.siterole_update(site_id, role_id, data=body)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    @staticmethod
    async def site_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        """
        if "offset" in kwargs:
            kwargs["offset"] = int(kwargs["offset"])
        if "limit" in kwargs:
            kwargs["limit"] = int(kwargs["limit"])
        if "site_ids" in kwargs:
            kwargs["site_ids"] = [int(site_id) for site_id in kwargs["site_ids"]]

        with client_exception_handler():
            sites = access_control_api.site_list(**kwargs)

        if sites:
            transform = transformations.SITE
            result = [transform.apply(site.to_dict()) for site in sites]
            return result

        return []

    @staticmethod
    async def site_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            site = access_control_api.site_create(data=body)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    @staticmethod
    async def site_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            result = access_control_api.site_delete(site_id)

        return result

    @staticmethod
    async def site_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            site = access_control_api.site_read(site_id)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    @staticmethod
    async def site_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            site = access_control_api.site_update(site_id, data=body)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    @staticmethod
    async def get__api_v1_sites_site_id_activate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_sites_site_id_deactivate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
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
        """
        # All but one parameter is an integer
        for key in ["offset", "limit", "domain_id", "role_id"]:
            if key in kwargs:
                kwargs[key] = int(kwargs[key])

        with client_exception_handler():
            udrs = access_control_api.userdomainrole_list(**kwargs)

        if udrs:
            transform = transformations.USER_DOMAIN_ROLE
            result = [transform.apply(udr.to_dict()) for udr in udrs]
            return result

        return []

    @staticmethod
    async def userdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            udr = access_control_api.userdomainrole_create(data=body)

        if udr:
            transform = transformations.USER_DOMAIN_ROLE
            result = transform.apply(udr.to_dict())
            return result

        return None

    @staticmethod
    async def userdomainrole_delete(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            result = access_control_api.userdomainrole_delete(user_id, domain_id, role_id)

        return result

    @staticmethod
    async def userdomainrole_read(request, user_id, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            udr = access_control_api.userdomainrole_read(user_id, domain_id, role_id)

        if udr:
            transform = transformations.USER_DOMAIN_ROLE
            result = transform.apply(udr.to_dict())
            return result

        return None

    @staticmethod
    async def user_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param email (optional): string An optional email filter
        :param user_ids (optional): array An optional list of user ids
        """
        if "offset" in kwargs:
            kwargs["offset"] = int(kwargs["offset"])
        if "limit" in kwargs:
            kwargs["limit"] = int(kwargs["limit"])

        raise NotImplementedError()

    @staticmethod
    async def user_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def user_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def user_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_users_user_id_activate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        raise NotImplementedError()

    @staticmethod
    async def get__api_v1_users_user_id_deactivate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
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
        """
        # All but one parameter is an integer
        for key in ["offset", "limit", "site_id"]:
            if key in kwargs:
                kwargs[key] = int(kwargs[key])

        with client_exception_handler():
            usds = user_data_api.usersitedata_list(**kwargs)

        if usds:
            transform = transformations.USER_SITE_DATA
            result = [transform.apply(usd.to_dict()) for usd in usds]
            return result

        return []

    @staticmethod
    async def usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            usd = user_data_api.usersitedata_create(data=body)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

        return None

    @staticmethod
    async def usersitedata_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            result = user_data_api.usersitedata_delete(user_id, site_id)

        return result

    @staticmethod
    async def usersitedata_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            usd = user_data_api.usersitedata_read(user_id, site_id)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

        return None

    @staticmethod
    async def usersitedata_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        with client_exception_handler():
            usd = user_data_api.usersitedata_update(user_id, site_id, data=body)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

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
        # All but one parameter is an integer
        for key in ["offset", "limit", "site_id", "role_id"]:
            if key in kwargs:
                kwargs[key] = int(kwargs[key])

        with client_exception_handler():
            usrs = access_control_api.usersiterole_list(**kwargs)

        if usrs:
            transform = transformations.USER_SITE_ROLE
            result = [transform.apply(usr.to_dict()) for usr in usrs]
            return result

        return []

    @staticmethod
    async def usersiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        with client_exception_handler():
            usr = access_control_api.usersiterole_create(data=body)

        if usr:
            transform = transformations.USER_SITE_ROLE
            result = transform.apply(usr.to_dict())
            return result

        return None

    @staticmethod
    async def usersiterole_delete(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            result = access_control_api.usersiterole_delete(user_id, site_id, role_id)

        return result

    @staticmethod
    async def usersiterole_read(request, user_id, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        """
        with client_exception_handler():
            usr = access_control_api.usersiterole_read(user_id, site_id, role_id)

        if usr:
            transform = transformations.USER_SITE_ROLE
            result = transform.apply(usr.to_dict())
            return result

        return None
