from management_layer.api.stubs import AbstractStubClass
from management_layer import transformations, mappings
from management_layer.utils import client_exception_handler
from management_layer.permission.decorator import require_permissions, requester_has_role

TOTAL_COUNT_HEADER = "X-Total-Count"
CLIENT_TOTAL_COUNT_HEADER = "Content-Length"  # TODO: Use correct header


class Implementation(AbstractStubClass):
    """
    The implementation linking calls made the Management Layer
    to the Authentication-, Access Control- and User Data Store services.
    """

    # adminnote_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:adminnote", "read")])
    async def adminnote_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :param creator_id (optional): string An optional query parameter to filter by creator (a user_id)
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
        with client_exception_handler():
            admin_note = await request.app["user_data_api"].adminnote_create(data=body)

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
                                                                             data=body)

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
        :param client_id: string A string value identifying the client
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            client = await request.app["authentication_service_api"].client_read(client_id)

        if client:
            transform = transformations.CLIENT
            result = transform.apply(client.to_dict())
            return result

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
            domain_role = await request.app["access_control_api"].domainrole_create(data=body)

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
            domain_role = await request.app["access_control_api"].domainrole_update(domain_id, role_id, data=body)

        if domain_role:
            transform = transformations.DOMAIN_ROLE
            result = transform.apply(domain_role.to_dict())
            return result

        return None

    # domain_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:domain", "read")])
    async def domain_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
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
            domain = await request.app["access_control_api"].domain_create(data=body)

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
    @require_permissions(all, [("urn:ge:access_control:domain", "read")])
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
            domain = await request.app["access_control_api"].domain_update(domain_id, data=body)

        if domain:
            transform = transformations.DOMAIN
            result = transform.apply(domain.to_dict())
            return result

        return None

    # invitationdomainrole_list -- Synchronisation point for meld
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

    # invitationdomainrole_create -- Synchronisation point for meld
    @staticmethod
    async def invitationdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationdomainrole_delete -- Synchronisation point for meld
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

    # invitationdomainrole_read -- Synchronisation point for meld
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

    # invitation_list -- Synchronisation point for meld
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

    # invitation_create -- Synchronisation point for meld
    @staticmethod
    async def invitation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitation_delete -- Synchronisation point for meld
    @staticmethod
    async def invitation_delete(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitation_read -- Synchronisation point for meld
    @staticmethod
    async def invitation_read(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitation_update -- Synchronisation point for meld
    @staticmethod
    async def invitation_update(request, body, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitation_id: string A UUID value identifying the invitation.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationsiterole_list -- Synchronisation point for meld
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

    # invitationsiterole_create -- Synchronisation point for meld
    @staticmethod
    async def invitationsiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationsiterole_delete -- Synchronisation point for meld
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

    # invitationsiterole_read -- Synchronisation point for meld
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

    # get_all_user_roles -- Synchronisation point for meld
    @staticmethod
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
    async def get_domain_roles(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            domain_roles = await request.app["operational_api"].get_domain_roles(domain_id)
            return domain_roles.to_dict()

    # get_site_and_domain_roles -- Synchronisation point for meld
    @staticmethod
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
    async def get_site_role_labels_aggregated(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            site_role_labels_aggregated = await request.app["operational_api"].get_site_role_labels_aggregated(site_id)
            return site_role_labels_aggregated.to_dict()

    # get_user_site_role_labels_aggregated -- Synchronisation point for meld
    @staticmethod
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
            permission = await request.app["access_control_api"].permission_create(data=body)

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
            permission = await request.app["access_control_api"].permission_update(permission_id, data=body)

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
            resource = await request.app["access_control_api"].resource_create(data=body)

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
            resource = await request.app["access_control_api"].resource_update(resource_id, data=body)

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
            rrp = await request.app["access_control_api"].roleresourcepermission_create(data=body)

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
            role = await request.app["access_control_api"].role_create(data=body)

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
            role = await request.app["access_control_api"].role_update(role_id, data=body)

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
            sds = await request.app["user_data_api"].sitedataschema_create(data=body)

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
            sds = await request.app["user_data_api"].sitedataschema_update(site_id, data=body)

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
            site_role = await request.app["access_control_api"].siterole_create(data=body)

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
            site_role = await request.app["access_control_api"].siterole_update(site_id, role_id, data=body)

        if site_role:
            transform = transformations.SITE_ROLE
            result = transform.apply(site_role.to_dict())
            return result

        return None

    # site_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:site", "read")])
    async def site_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
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
            site = await request.app["access_control_api"].site_create(data=body)

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
    @require_permissions(all, [("urn:ge:access_control:site", "read")])
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
            site = await request.app["access_control_api"].site_update(site_id, data=body)

        if site:
            transform = transformations.SITE
            result = transform.apply(site.to_dict())
            return result

        return None

    # get__api_v1_sites_site_id_activate -- Synchronisation point for meld
    @staticmethod
    async def get__api_v1_sites_site_id_activate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get__api_v1_sites_site_id_deactivate -- Synchronisation point for meld
    @staticmethod
    async def get__api_v1_sites_site_id_deactivate(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # userdomainrole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:userdomainrole", "read")])
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
            udr = await request.app["access_control_api"].userdomainrole_create(data=body)

        if udr:
            transform = transformations.USER_DOMAIN_ROLE
            result = transform.apply(udr.to_dict())
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
    @require_permissions(all, [("urn:ge:access_control:userdomainrole", "read")])
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
        :param email (optional): string An optional email filter
        :param username_prefix (optional): string An optional username prefix filter
        :param user_ids (optional): array An optional list of user ids
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
    @require_permissions(all, [("urn:ge:identity_provider:user", "read")])
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
    @require_permissions(all, [("urn:ge:identity_provider:user", "update")])
    async def user_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            user = await request.app["authentication_service_api"].user_update(user_id, data=body)

        if user:
            transform = transformations.USER
            result = transform.apply(user.to_dict())
            return result

        return None

    # get__api_v1_users_user_id_activate -- Synchronisation point for meld
    @staticmethod
    async def get__api_v1_users_user_id_activate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get__api_v1_users_user_id_deactivate -- Synchronisation point for meld
    @staticmethod
    async def get__api_v1_users_user_id_deactivate(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # usersitedata_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "read")])
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
    async def usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usd = await request.app["user_data_api"].usersitedata_create(data=body)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

        return None

    # usersitedata_delete -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "delete")])
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
    @require_permissions(all, [("urn:ge:user_data:usersitedata", "read")])
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
    async def usersitedata_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        with client_exception_handler():
            usd = await request.app["user_data_api"].usersitedata_update(user_id, site_id, data=body)

        if usd:
            transform = transformations.USER_SITE_DATA
            result = transform.apply(usd.to_dict())
            return result

    # usersiterole_list -- Synchronisation point for meld
    @staticmethod
    @require_permissions(all, [("urn:ge:access_control:usersiterole", "read")])
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
            usr = await request.app["access_control_api"].usersiterole_create(data=body)

        if usr:
            transform = transformations.USER_SITE_ROLE
            result = transform.apply(usr.to_dict())
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
    @require_permissions(all, [("urn:ge:access_control:usersiterole", "read")])
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
