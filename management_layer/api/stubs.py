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

    # adminnote_list -- Synchronisation point for meld
    @staticmethod
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
        raise NotImplementedError()

    # adminnote_create -- Synchronisation point for meld
    @staticmethod
    async def adminnote_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # adminnote_delete -- Synchronisation point for meld
    @staticmethod
    async def adminnote_delete(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # adminnote_read -- Synchronisation point for meld
    @staticmethod
    async def adminnote_read(request, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # adminnote_update -- Synchronisation point for meld
    @staticmethod
    async def adminnote_update(request, body, admin_note_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param admin_note_id: integer A unique integer value identifying the admin note.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # client_list -- Synchronisation point for meld
    @staticmethod
    async def client_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param client_ids (optional): array An optional list of client ids
        :param client_token_id (optional): string An optional client id to filter on. This is not the primary key.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # client_read -- Synchronisation point for meld
    @staticmethod
    async def client_read(request, client_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_id: integer A integer identifying the client
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # country_list -- Synchronisation point for meld
    @staticmethod
    async def country_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param country_codes (optional): array An optional list of country codes
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # country_read -- Synchronisation point for meld
    @staticmethod
    async def country_read(request, country_code, **kwargs):
        """
        :param request: An HttpRequest
        :param country_code: string A unique two-character value identifying the country.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # credentials_list -- Synchronisation point for meld
    @staticmethod
    async def credentials_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param credentials_ids (optional): array An optional list of credentials ids
        :param site_id (optional): integer An optional query parameter to filter by site_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # credentials_create -- Synchronisation point for meld
    @staticmethod
    async def credentials_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # credentials_delete -- Synchronisation point for meld
    @staticmethod
    async def credentials_delete(request, credentials_id, **kwargs):
        """
        :param request: An HttpRequest
        :param credentials_id: integer A unique integer value identifying the credentials.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # credentials_read -- Synchronisation point for meld
    @staticmethod
    async def credentials_read(request, credentials_id, **kwargs):
        """
        :param request: An HttpRequest
        :param credentials_id: integer A unique integer value identifying the credentials.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # credentials_update -- Synchronisation point for meld
    @staticmethod
    async def credentials_update(request, body, credentials_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param credentials_id: integer A unique integer value identifying the credentials.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteduser_list -- Synchronisation point for meld
    @staticmethod
    async def deleteduser_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param deleter_id (optional): string An optional query parameter to filter by deleter_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteduser_create -- Synchronisation point for meld
    @staticmethod
    async def deleteduser_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteduser_delete -- Synchronisation point for meld
    @staticmethod
    async def deleteduser_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteduser_read -- Synchronisation point for meld
    @staticmethod
    async def deleteduser_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deleteduser_update -- Synchronisation point for meld
    @staticmethod
    async def deleteduser_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletedusersite_list -- Synchronisation point for meld
    @staticmethod
    async def deletedusersite_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletedusersite_create -- Synchronisation point for meld
    @staticmethod
    async def deletedusersite_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletedusersite_delete -- Synchronisation point for meld
    @staticmethod
    async def deletedusersite_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletedusersite_read -- Synchronisation point for meld
    @staticmethod
    async def deletedusersite_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletedusersite_update -- Synchronisation point for meld
    @staticmethod
    async def deletedusersite_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletionmethod_list -- Synchronisation point for meld
    @staticmethod
    async def deletionmethod_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletionmethod_create -- Synchronisation point for meld
    @staticmethod
    async def deletionmethod_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletionmethod_delete -- Synchronisation point for meld
    @staticmethod
    async def deletionmethod_delete(request, deletionmethod_id, **kwargs):
        """
        :param request: An HttpRequest
        :param deletionmethod_id: integer A unique integer value identifying the credentials.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletionmethod_read -- Synchronisation point for meld
    @staticmethod
    async def deletionmethod_read(request, deletionmethod_id, **kwargs):
        """
        :param request: An HttpRequest
        :param deletionmethod_id: integer A unique integer value identifying the credentials.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # deletionmethod_update -- Synchronisation point for meld
    @staticmethod
    async def deletionmethod_update(request, body, deletionmethod_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param deletionmethod_id: integer A unique integer value identifying the credentials.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domainrole_list -- Synchronisation point for meld
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

    # domainrole_create -- Synchronisation point for meld
    @staticmethod
    async def domainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domainrole_delete -- Synchronisation point for meld
    @staticmethod
    async def domainrole_delete(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domainrole_read -- Synchronisation point for meld
    @staticmethod
    async def domainrole_read(request, domain_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domainrole_update -- Synchronisation point for meld
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

    # domain_list -- Synchronisation point for meld
    @staticmethod
    async def domain_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param parent_id (optional): integer An optional query parameter to filter by parent_id
        :param domain_ids (optional): array An optional list of domain ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domain_create -- Synchronisation point for meld
    @staticmethod
    async def domain_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domain_delete -- Synchronisation point for meld
    @staticmethod
    async def domain_delete(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domain_read -- Synchronisation point for meld
    @staticmethod
    async def domain_read(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # domain_update -- Synchronisation point for meld
    @staticmethod
    async def domain_update(request, body, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # event_create -- Synchronisation point for meld
    @staticmethod
    async def event_create(request, body, account_id, event_type, signature, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param account_id: string 
        :param event_type: string 
        :param signature: string 
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # healthcheck -- Synchronisation point for meld
    @staticmethod
    async def healthcheck(request, **kwargs):
        """
        :param request: An HttpRequest
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

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

    # invitationredirecturl_list -- Synchronisation point for meld
    @staticmethod
    async def invitationredirecturl_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitationredirecturl_ids (optional): array An optional list of invitationredirecturl ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationredirecturl_create -- Synchronisation point for meld
    @staticmethod
    async def invitationredirecturl_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationredirecturl_delete -- Synchronisation point for meld
    @staticmethod
    async def invitationredirecturl_delete(request, invitationredirecturl_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitationredirecturl_id: integer A unique integer value identifying the redirect URL.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationredirecturl_read -- Synchronisation point for meld
    @staticmethod
    async def invitationredirecturl_read(request, invitationredirecturl_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitationredirecturl_id: integer A unique integer value identifying the redirect URL.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # invitationredirecturl_update -- Synchronisation point for meld
    @staticmethod
    async def invitationredirecturl_update(request, body, invitationredirecturl_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitationredirecturl_id: integer A unique integer value identifying the redirect URL.
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

    # invitation_send -- Synchronisation point for meld
    @staticmethod
    async def invitation_send(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string 
        :param language (optional): string 
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # purge_expired_invitations -- Synchronisation point for meld
    @staticmethod
    async def purge_expired_invitations(request, **kwargs):
        """
        :param request: An HttpRequest
        :param synchronous_mode (optional): boolean Change the mode of the call to synchronous.
        :param cutoff_date (optional): string An optional cutoff date to purge invites before this date
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
        raise NotImplementedError()

    # confirm_user_data_deletion -- Synchronisation point for meld
    @staticmethod
    async def confirm_user_data_deletion(request, user_id, account_id, signature, nonce, expiry, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param account_id: string 
        :param signature: string 
        :param nonce: string 
        :param expiry: integer 
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_domain_roles -- Synchronisation point for meld
    @staticmethod
    async def get_domain_roles(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_site_from_client_token_id -- Synchronisation point for meld
    @staticmethod
    async def get_site_from_client_token_id(request, client_token_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_token_id: string A client token id. This is not the primary key of the client table, but rather the client id that is typically configured along with the client secret.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_sites_under_domain -- Synchronisation point for meld
    @staticmethod
    async def get_sites_under_domain(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_site_and_domain_roles -- Synchronisation point for meld
    @staticmethod
    async def get_site_and_domain_roles(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_site_role_labels_aggregated -- Synchronisation point for meld
    @staticmethod
    async def get_site_role_labels_aggregated(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_user_domain_permissions -- Synchronisation point for meld
    @staticmethod
    async def get_user_domain_permissions(request, user_id, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # user_has_permissions -- Synchronisation point for meld
    @staticmethod
    async def user_has_permissions(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_user_management_portal_permissions -- Synchronisation point for meld
    @staticmethod
    async def get_user_management_portal_permissions(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_user_site_permissions -- Synchronisation point for meld
    @staticmethod
    async def get_user_site_permissions(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_user_site_role_labels_aggregated -- Synchronisation point for meld
    @staticmethod
    async def get_user_site_role_labels_aggregated(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_users_with_roles_for_domain -- Synchronisation point for meld
    @staticmethod
    async def get_users_with_roles_for_domain(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # get_users_with_roles_for_site -- Synchronisation point for meld
    @staticmethod
    async def get_users_with_roles_for_site(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # implicit_usersitedata_read -- Synchronisation point for meld
    @staticmethod
    async def implicit_usersitedata_read(request, **kwargs):
        """
        :param request: An HttpRequest
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # implicit_usersitedata_create -- Synchronisation point for meld
    @staticmethod
    async def implicit_usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # implicit_usersitedata_update -- Synchronisation point for meld
    @staticmethod
    async def implicit_usersitedata_update(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # organisation_list -- Synchronisation point for meld
    @staticmethod
    async def organisation_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param organisation_ids (optional): array An optional list of organisation ids
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # organisation_create -- Synchronisation point for meld
    @staticmethod
    async def organisation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # organisation_delete -- Synchronisation point for meld
    @staticmethod
    async def organisation_delete(request, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param organisation_id: integer An integer identifying an organisation
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # organisation_read -- Synchronisation point for meld
    @staticmethod
    async def organisation_read(request, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param organisation_id: integer An integer identifying an organisation
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # organisation_update -- Synchronisation point for meld
    @staticmethod
    async def organisation_update(request, body, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param organisation_id: integer An integer identifying an organisation
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # permission_list -- Synchronisation point for meld
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

    # permission_create -- Synchronisation point for meld
    @staticmethod
    async def permission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # permission_delete -- Synchronisation point for meld
    @staticmethod
    async def permission_delete(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # permission_read -- Synchronisation point for meld
    @staticmethod
    async def permission_read(request, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # permission_update -- Synchronisation point for meld
    @staticmethod
    async def permission_update(request, body, permission_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param permission_id: integer A unique integer value identifying the permission.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_all -- Synchronisation point for meld
    @staticmethod
    async def refresh_all(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_clients -- Synchronisation point for meld
    @staticmethod
    async def refresh_clients(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_credentials -- Synchronisation point for meld
    @staticmethod
    async def refresh_credentials(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_domains -- Synchronisation point for meld
    @staticmethod
    async def refresh_domains(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_keys -- Synchronisation point for meld
    @staticmethod
    async def refresh_keys(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_permissions -- Synchronisation point for meld
    @staticmethod
    async def refresh_permissions(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_resources -- Synchronisation point for meld
    @staticmethod
    async def refresh_resources(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_roles -- Synchronisation point for meld
    @staticmethod
    async def refresh_roles(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # refresh_sites -- Synchronisation point for meld
    @staticmethod
    async def refresh_sites(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # request_user_deletion -- Synchronisation point for meld
    @staticmethod
    async def request_user_deletion(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # resource_list -- Synchronisation point for meld
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

    # resource_create -- Synchronisation point for meld
    @staticmethod
    async def resource_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # resource_delete -- Synchronisation point for meld
    @staticmethod
    async def resource_delete(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # resource_read -- Synchronisation point for meld
    @staticmethod
    async def resource_read(request, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # resource_update -- Synchronisation point for meld
    @staticmethod
    async def resource_update(request, body, resource_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param resource_id: integer A unique integer value identifying the resource.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # roleresourcepermission_list -- Synchronisation point for meld
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

    # roleresourcepermission_create -- Synchronisation point for meld
    @staticmethod
    async def roleresourcepermission_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # roleresourcepermission_delete -- Synchronisation point for meld
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

    # roleresourcepermission_read -- Synchronisation point for meld
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

    # role_list -- Synchronisation point for meld
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

    # role_create -- Synchronisation point for meld
    @staticmethod
    async def role_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # role_delete -- Synchronisation point for meld
    @staticmethod
    async def role_delete(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # role_read -- Synchronisation point for meld
    @staticmethod
    async def role_read(request, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # role_update -- Synchronisation point for meld
    @staticmethod
    async def role_update(request, body, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # sitedataschema_list -- Synchronisation point for meld
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

    # sitedataschema_create -- Synchronisation point for meld
    @staticmethod
    async def sitedataschema_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # sitedataschema_delete -- Synchronisation point for meld
    @staticmethod
    async def sitedataschema_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # sitedataschema_read -- Synchronisation point for meld
    @staticmethod
    async def sitedataschema_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # sitedataschema_update -- Synchronisation point for meld
    @staticmethod
    async def sitedataschema_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # siterole_list -- Synchronisation point for meld
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

    # siterole_create -- Synchronisation point for meld
    @staticmethod
    async def siterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # siterole_delete -- Synchronisation point for meld
    @staticmethod
    async def siterole_delete(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # siterole_read -- Synchronisation point for meld
    @staticmethod
    async def siterole_read(request, site_id, role_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :param role_id: integer A unique integer value identifying the role.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # siterole_update -- Synchronisation point for meld
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

    # site_list -- Synchronisation point for meld
    @staticmethod
    async def site_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param site_ids (optional): array An optional list of site ids
        :param client_id (optional): integer An optional client id to filter on
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # site_create -- Synchronisation point for meld
    @staticmethod
    async def site_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # site_delete -- Synchronisation point for meld
    @staticmethod
    async def site_delete(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # site_read -- Synchronisation point for meld
    @staticmethod
    async def site_read(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # site_update -- Synchronisation point for meld
    @staticmethod
    async def site_update(request, body, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # userdomainrole_list -- Synchronisation point for meld
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

    # userdomainrole_create -- Synchronisation point for meld
    @staticmethod
    async def userdomainrole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # userdomainrole_delete -- Synchronisation point for meld
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

    # userdomainrole_read -- Synchronisation point for meld
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

    # user_list -- Synchronisation point for meld
    @staticmethod
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
        raise NotImplementedError()

    # user_delete -- Synchronisation point for meld
    @staticmethod
    async def user_delete(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # user_read -- Synchronisation point for meld
    @staticmethod
    async def user_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # user_update -- Synchronisation point for meld
    @staticmethod
    async def user_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # usersitedata_list -- Synchronisation point for meld
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

    # usersitedata_create -- Synchronisation point for meld
    @staticmethod
    async def usersitedata_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # usersitedata_delete -- Synchronisation point for meld
    @staticmethod
    async def usersitedata_delete(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # usersitedata_read -- Synchronisation point for meld
    @staticmethod
    async def usersitedata_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # usersitedata_update -- Synchronisation point for meld
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

    # usersiterole_list -- Synchronisation point for meld
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

    # usersiterole_create -- Synchronisation point for meld
    @staticmethod
    async def usersiterole_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :returns: result or (result, headers) tuple
        """
        raise NotImplementedError()

    # usersiterole_delete -- Synchronisation point for meld
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

    # usersiterole_read -- Synchronisation point for meld
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
        :param admin_note_ids (optional): array An optional list of adminnote ids
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
                "type": "string",
                "x-related-info": {
                    "label": "username",
                    "model": "user"
                }
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
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
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
        :param client_token_id (optional): string An optional client id to filter on. This is not the primary key.
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
                "type": "string",
                "x-related-info": {
                    "model": null
                }
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
                "format": "uri",
                "type": "string"
            },
            "website_url": {
                "description": "",
                "format": "uri",
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
        :param client_id: integer A integer identifying the client
        """
        response_schema = schemas.client
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def country_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param country_codes (optional): array An optional list of country codes
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "code": {
                "maxLength": 2,
                "minLength": 2,
                "type": "string"
            },
            "name": {
                "maxLength": 100,
                "type": "string"
            }
        },
        "required": [
            "code",
            "name"
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
    async def country_read(request, country_code, **kwargs):
        """
        :param request: An HttpRequest
        :param country_code: string A unique two-character value identifying the country.
        """
        response_schema = schemas.country
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def credentials_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param credentials_ids (optional): array An optional list of credentials ids
        :param site_id (optional): integer An optional query parameter to filter by site_id
        """
        response_schema = json.loads("""{
    "items": {
        "description": "An object containing account credentials",
        "properties": {
            "account_id": {
                "maxLength": 256,
                "minLength": 32,
                "type": "string"
            },
            "account_secret": {
                "maxLength": 256,
                "minLength": 32,
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "updated_at": {
                "format": "date-time",
                "type": "string"
            }
        },
        "required": [
            "id",
            "site_id",
            "account_id",
            "account_secret",
            "description",
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
    async def credentials_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.credentials
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def credentials_delete(request, credentials_id, **kwargs):
        """
        :param request: An HttpRequest
        :param credentials_id: integer A unique integer value identifying the credentials.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def credentials_read(request, credentials_id, **kwargs):
        """
        :param request: An HttpRequest
        :param credentials_id: integer A unique integer value identifying the credentials.
        """
        response_schema = schemas.credentials
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def credentials_update(request, body, credentials_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param credentials_id: integer A unique integer value identifying the credentials.
        """
        response_schema = schemas.credentials
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deleteduser_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param deleter_id (optional): string An optional query parameter to filter by deleter_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "deleted_at": {
                "format": "date-time",
                "type": "string"
            },
            "deleter_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username",
                    "model": "user"
                }
            },
            "email": {
                "format": "email",
                "type": "string"
            },
            "id": {
                "format": "uuid",
                "type": "string"
            },
            "msisdn": {
                "type": "string"
            },
            "reason": {
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "username": {
                "type": "string"
            }
        },
        "required": [
            "id",
            "username",
            "reason",
            "created_at",
            "updated_at",
            "deleter_id"
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
    async def deleteduser_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.deleted_user
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deleteduser_delete(request, user_id, **kwargs):
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
    async def deleteduser_read(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.deleted_user
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deleteduser_update(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.deleted_user
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletedusersite_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param user_id (optional): string An optional query parameter to filter by user_id
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "deleted_user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username",
                    "model": "deleted_user"
                }
            },
            "deletion_confirmed_at": {
                "format": "date-time",
                "type": "string"
            },
            "deletion_confirmed_via": {
                "type": "string"
            },
            "deletion_requested_at": {
                "format": "date-time",
                "type": "string"
            },
            "deletion_requested_via": {
                "type": "string"
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "site"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "deleted_user_id",
            "site_id",
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
    async def deletedusersite_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.deleted_user_site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletedusersite_delete(request, user_id, site_id, **kwargs):
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
    async def deletedusersite_read(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.deleted_user_site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletedusersite_update(request, body, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = schemas.deleted_user_site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletionmethod_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "data_schema": {
                "type": "object"
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
            "label",
            "data_schema",
            "description",
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
    async def deletionmethod_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.deletion_method
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletionmethod_delete(request, deletionmethod_id, **kwargs):
        """
        :param request: An HttpRequest
        :param deletionmethod_id: integer A unique integer value identifying the credentials.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletionmethod_read(request, deletionmethod_id, **kwargs):
        """
        :param request: An HttpRequest
        :param deletionmethod_id: integer A unique integer value identifying the credentials.
        """
        response_schema = schemas.deletion_method
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def deletionmethod_update(request, body, deletionmethod_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param deletionmethod_id: integer A unique integer value identifying the credentials.
        """
        response_schema = schemas.deletion_method
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "grant_implicitly": {
                "type": "boolean"
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
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
        :param parent_id (optional): integer An optional query parameter to filter by parent_id
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
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "domain"
                }
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
    async def event_create(request, body, account_id, event_type, signature, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param account_id: string 
        :param event_type: string 
        :param signature: string 
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def healthcheck(request, **kwargs):
        """
        :param request: An HttpRequest
        """
        response_schema = schemas.health_info
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "invitation_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "email"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
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
    async def invitationredirecturl_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param invitationredirecturl_ids (optional): array An optional list of invitationredirecturl ids
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
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "url": {
                "format": "uri",
                "type": "string"
            }
        },
        "required": [
            "id",
            "url",
            "description",
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
    async def invitationredirecturl_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.invitation_redirect_url
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationredirecturl_delete(request, invitationredirecturl_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitationredirecturl_id: integer A unique integer value identifying the redirect URL.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationredirecturl_read(request, invitationredirecturl_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitationredirecturl_id: integer A unique integer value identifying the redirect URL.
        """
        response_schema = schemas.invitation_redirect_url
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def invitationredirecturl_update(request, body, invitationredirecturl_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param invitationredirecturl_id: integer A unique integer value identifying the redirect URL.
        """
        response_schema = schemas.invitation_redirect_url
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
            "invitation_redirect_url_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "url",
                    "model": "invitation_redirect_url"
                }
            },
            "invitor_id": {
                "description": "The user that created the invitation",
                "format": "uuid",
                "readOnly": true,
                "type": "string",
                "x-related-info": {
                    "label": "username",
                    "model": "user"
                }
            },
            "last_name": {
                "maxLength": 100,
                "type": "string"
            },
            "organisation_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "organisation"
                }
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
            "organisation_id",
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
    async def invitation_send(request, invitation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param invitation_id: string 
        :param language (optional): string 
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def purge_expired_invitations(request, **kwargs):
        """
        :param request: An HttpRequest
        :param synchronous_mode (optional): boolean Change the mode of the call to synchronous.
        :param cutoff_date (optional): string An optional cutoff date to purge invites before this date
        """
        response_schema = schemas.purged_invitations
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
                "type": "string",
                "x-related-info": {
                    "label": "email"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
    async def confirm_user_data_deletion(request, user_id, account_id, signature, nonce, expiry, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param account_id: string 
        :param signature: string 
        :param nonce: string 
        :param expiry: integer 
        """
        response_schema = schemas.__UNSPECIFIED__
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
    async def get_site_from_client_token_id(request, client_token_id, **kwargs):
        """
        :param request: An HttpRequest
        :param client_token_id: string A client token id. This is not the primary key of the client table, but rather the client id that is typically configured along with the client secret.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.site
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_sites_under_domain(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "client_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "deletion_method_data": {
                "type": "object"
            },
            "deletion_method_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "description": {
                "type": "string"
            },
            "domain_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "is_active": {
                "type": "boolean"
            },
            "name": {
                "maxLength": 30,
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
            "deletion_method_id",
            "deletion_method_data",
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
    async def get_user_domain_permissions(request, user_id, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param domain_id: integer A unique integer value identifying the domain.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = json.loads("""{
    "items": {
        "type": "string"
    },
    "type": "array",
    "uniqueItems": true
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def user_has_permissions(request, body, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param user_id: string A UUID value identifying the user.
        """
        response_schema = schemas.user_permissions_check_response
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_user_management_portal_permissions(request, user_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = json.loads("""{
    "items": {
        "type": "string"
    },
    "type": "array",
    "uniqueItems": true
}""")
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def get_user_site_permissions(request, user_id, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param user_id: string A UUID value identifying the user.
        :param site_id: integer A unique integer value identifying the site.
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = json.loads("""{
    "items": {
        "type": "string"
    },
    "type": "array",
    "uniqueItems": true
}""")
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
    async def get_users_with_roles_for_domain(request, domain_id, **kwargs):
        """
        :param request: An HttpRequest
        :param domain_id: integer A unique integer value identifying the domain.
        """
        response_schema = json.loads("""{
    "items": {
        "description": "A user with their roles.",
        "properties": {
            "id": {
                "format": "uuid",
                "type": "string"
            },
            "roles": {
                "items": {
                    "type": "string"
                },
                "type": "array"
            },
            "username": {
                "type": "string"
            }
        },
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
    async def get_users_with_roles_for_site(request, site_id, **kwargs):
        """
        :param request: An HttpRequest
        :param site_id: integer A unique integer value identifying the site.
        """
        response_schema = json.loads("""{
    "items": {
        "description": "A user with their roles.",
        "properties": {
            "id": {
                "format": "uuid",
                "type": "string"
            },
            "roles": {
                "items": {
                    "type": "string"
                },
                "type": "array"
            },
            "username": {
                "type": "string"
            }
        },
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
    async def implicit_usersitedata_read(request, **kwargs):
        """
        :param request: An HttpRequest
        """
        response_schema = schemas.user_site_data
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def implicit_usersitedata_create(request, body, **kwargs):
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
    async def implicit_usersitedata_update(request, body, **kwargs):
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
    async def organisation_list(request, **kwargs):
        """
        :param request: An HttpRequest
        :param offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
        :param limit (optional): integer An optional query parameter to limit the number of results returned.
        :param organisation_ids (optional): array An optional list of organisation ids
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
                "type": "integer"
            },
            "name": {
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
            "description",
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
    async def organisation_create(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.organisation
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def organisation_delete(request, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param organisation_id: integer An integer identifying an organisation
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def organisation_read(request, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param organisation_id: integer An integer identifying an organisation
        """
        response_schema = schemas.organisation
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def organisation_update(request, body, organisation_id, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        :param organisation_id: integer An integer identifying an organisation
        """
        response_schema = schemas.organisation
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
    async def refresh_all(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_clients(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_credentials(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_domains(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_keys(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_permissions(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_resources(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_roles(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def refresh_sites(request, **kwargs):
        """
        :param request: An HttpRequest
        :param nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
        """
        response_schema = schemas.__UNSPECIFIED__
        if "type" not in response_schema:
            response_schema["type"] = "object"

        if response_schema["type"] == "array" and "type" not in response_schema["items"]:
            response_schema["items"]["type"] = "object"

        return MockedStubClass.GENERATOR.random_value(response_schema)

    @staticmethod
    async def request_user_deletion(request, body, **kwargs):
        """
        :param request: An HttpRequest
        :param body: dict A dictionary containing the parsed and validated body
        """
        response_schema = schemas.__UNSPECIFIED__
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "resource_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "urn"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
        :param client_id (optional): integer An optional client id to filter on
        """
        response_schema = json.loads("""{
    "items": {
        "properties": {
            "client_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "deletion_method_data": {
                "type": "object"
            },
            "deletion_method_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "description": {
                "type": "string"
            },
            "domain_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "is_active": {
                "type": "boolean"
            },
            "name": {
                "maxLength": 30,
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
            "deletion_method_id",
            "deletion_method_data",
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
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
                "type": "string",
                "x-related-info": {
                    "field": "code",
                    "label": "name",
                    "model": "country"
                }
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "date_joined": {
                "description": "",
                "format": "date-time",
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
            "organisation_id": {
                "readOnly": true,
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "organisation"
                }
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
        response_schema = schemas.user
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
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "data": {
                "type": "object"
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
            }
        },
        "required": [
            "user_id",
            "site_id",
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
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
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
