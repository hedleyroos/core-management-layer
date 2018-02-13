# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
###
### The code is auto generated, your change will be overwritten by
### code generating.
###
from __future__ import absolute_import

from .api.ops_site_role_labels_aggregated_site_id import OpsSiteRoleLabelsAggregatedSiteId
from .api.ops_user_site_role_labels_aggregated_user_id_site_id import OpsUserSiteRoleLabelsAggregatedUserIdSiteId
from .api.ops_domain_roles_domain_id import OpsDomainRolesDomainId
from .api.ops_site_and_domain_roles_site_id import OpsSiteAndDomainRolesSiteId
from .api.ops_all_user_roles_user_id import OpsAllUserRolesUserId
from .api.domains import Domains
from .api.domains_domain_id import DomainsDomainId
from .api.domainroles import Domainroles
from .api.domainroles_domain_id_role_id import DomainrolesDomainIdRoleId
from .api.invitations import Invitations
from .api.invitations_invitation_id import InvitationsInvitationId
from .api.invitationdomainroles import Invitationdomainroles
from .api.invitationdomainroles_invitation_id_domain_id_role_id import InvitationdomainrolesInvitationIdDomainIdRoleId
from .api.invitationsiteroles import Invitationsiteroles
from .api.invitationsiteroles_invitation_id_site_id_role_id import InvitationsiterolesInvitationIdSiteIdRoleId
from .api.permissions import Permissions
from .api.permissions_permission_id import PermissionsPermissionId
from .api.resources import Resources
from .api.resources_resource_id import ResourcesResourceId
from .api.roles import Roles
from .api.roles_role_id import RolesRoleId
from .api.roleresourcepermissions import Roleresourcepermissions
from .api.roleresourcepermissions_role_id_resource_id_permission_id import RoleresourcepermissionsRoleIdResourceIdPermissionId
from .api.sites import Sites
from .api.sites_site_id import SitesSiteId
from .api.siteroles import Siteroles
from .api.siteroles_site_id_role_id import SiterolesSiteIdRoleId
from .api.userdomainroles import Userdomainroles
from .api.userdomainroles_user_id_domain_id_role_id import UserdomainrolesUserIdDomainIdRoleId
from .api.usersiteroles import Usersiteroles
from .api.usersitedata import Usersitedata
from .api.usersitedata_user_id_site_id import UsersitedataUserIdSiteId
from .api.adminnotes import Adminnotes
from .api.adminnotes_user_id_creator_id_created_at import AdminnotesUserIdCreatorIdCreatedAt
from .api.sitedataschemas import Sitedataschemas
from .api.sitedataschemas_site_id import SitedataschemasSiteId
from .api.clients import Clients
from .api.clients_client_id import ClientsClientId
from .api.users import Users
from .api.users_user_id import UsersUserId
from .api.users_user_id_activate import UsersUserIdActivate
from .api.users_user_id_deactivate import UsersUserIdDeactivate
from .api.sites_site_id_activate import SitesSiteIdActivate
from .api.sites_site_id_deactivate import SitesSiteIdDeactivate


url_prefix = 'api/v1'

routes = [
    dict(resource=OpsSiteRoleLabelsAggregatedSiteId, urls=[r"/ops/site_role_labels_aggregated/(?P<site_id>[^/]+?)"], endpoint='ops_site_role_labels_aggregated_site_id'),
    dict(resource=OpsUserSiteRoleLabelsAggregatedUserIdSiteId, urls=[r"/ops/user_site_role_labels_aggregated/(?P<user_id>[^/]+?)/(?P<site_id>[^/]+?)"], endpoint='ops_user_site_role_labels_aggregated_user_id_site_id'),
    dict(resource=OpsDomainRolesDomainId, urls=[r"/ops/domain_roles/(?P<domain_id>[^/]+?)"], endpoint='ops_domain_roles_domain_id'),
    dict(resource=OpsSiteAndDomainRolesSiteId, urls=[r"/ops/site_and_domain_roles/(?P<site_id>[^/]+?)"], endpoint='ops_site_and_domain_roles_site_id'),
    dict(resource=OpsAllUserRolesUserId, urls=[r"/ops/all_user_roles/(?P<user_id>[^/]+?)"], endpoint='ops_all_user_roles_user_id'),
    dict(resource=Domains, urls=[r"/domains"], endpoint='domains'),
    dict(resource=DomainsDomainId, urls=[r"/domains/(?P<domain_id>[^/]+?)"], endpoint='domains_domain_id'),
    dict(resource=Domainroles, urls=[r"/domainroles"], endpoint='domainroles'),
    dict(resource=DomainrolesDomainIdRoleId, urls=[r"/domainroles/(?P<domain_id>[^/]+?)/(?P<role_id>[^/]+?)"], endpoint='domainroles_domain_id_role_id'),
    dict(resource=Invitations, urls=[r"/invitations"], endpoint='invitations'),
    dict(resource=InvitationsInvitationId, urls=[r"/invitations/(?P<invitation_id>[^/]+?)"], endpoint='invitations_invitation_id'),
    dict(resource=Invitationdomainroles, urls=[r"/invitationdomainroles"], endpoint='invitationdomainroles'),
    dict(resource=InvitationdomainrolesInvitationIdDomainIdRoleId, urls=[r"/invitationdomainroles/(?P<invitation_id>[^/]+?)/(?P<domain_id>[^/]+?)/(?P<role_id>[^/]+?)"], endpoint='invitationdomainroles_invitation_id_domain_id_role_id'),
    dict(resource=Invitationsiteroles, urls=[r"/invitationsiteroles"], endpoint='invitationsiteroles'),
    dict(resource=InvitationsiterolesInvitationIdSiteIdRoleId, urls=[r"/invitationsiteroles/(?P<invitation_id>[^/]+?)/(?P<site_id>[^/]+?)/(?P<role_id>[^/]+?)"], endpoint='invitationsiteroles_invitation_id_site_id_role_id'),
    dict(resource=Permissions, urls=[r"/permissions"], endpoint='permissions'),
    dict(resource=PermissionsPermissionId, urls=[r"/permissions/(?P<permission_id>[^/]+?)"], endpoint='permissions_permission_id'),
    dict(resource=Resources, urls=[r"/resources"], endpoint='resources'),
    dict(resource=ResourcesResourceId, urls=[r"/resources/(?P<resource_id>[^/]+?)"], endpoint='resources_resource_id'),
    dict(resource=Roles, urls=[r"/roles"], endpoint='roles'),
    dict(resource=RolesRoleId, urls=[r"/roles/(?P<role_id>[^/]+?)"], endpoint='roles_role_id'),
    dict(resource=Roleresourcepermissions, urls=[r"/roleresourcepermissions"], endpoint='roleresourcepermissions'),
    dict(resource=RoleresourcepermissionsRoleIdResourceIdPermissionId, urls=[r"/roleresourcepermissions/(?P<role_id>[^/]+?)/(?P<resource_id>[^/]+?)/(?P<permission_id>[^/]+?)"], endpoint='roleresourcepermissions_role_id_resource_id_permission_id'),
    dict(resource=Sites, urls=[r"/sites"], endpoint='sites'),
    dict(resource=SitesSiteId, urls=[r"/sites/(?P<site_id>[^/]+?)"], endpoint='sites_site_id'),
    dict(resource=Siteroles, urls=[r"/siteroles"], endpoint='siteroles'),
    dict(resource=SiterolesSiteIdRoleId, urls=[r"/siteroles/(?P<site_id>[^/]+?)/(?P<role_id>[^/]+?)"], endpoint='siteroles_site_id_role_id'),
    dict(resource=Userdomainroles, urls=[r"/userdomainroles"], endpoint='userdomainroles'),
    dict(resource=UserdomainrolesUserIdDomainIdRoleId, urls=[r"/userdomainroles/(?P<user_id>[^/]+?)/(?P<domain_id>[^/]+?)/(?P<role_id>[^/]+?)"], endpoint='userdomainroles_user_id_domain_id_role_id'),
    dict(resource=Usersiteroles, urls=[r"/usersiteroles"], endpoint='usersiteroles'),
    dict(resource=Usersitedata, urls=[r"/usersitedata"], endpoint='usersitedata'),
    dict(resource=UsersitedataUserIdSiteId, urls=[r"/usersitedata/(?P<user_id>[^/]+?)/(?P<site_id>[^/]+?)"], endpoint='usersitedata_user_id_site_id'),
    dict(resource=Adminnotes, urls=[r"/adminnotes"], endpoint='adminnotes'),
    dict(resource=AdminnotesUserIdCreatorIdCreatedAt, urls=[r"/adminnotes/(?P<user_id>[^/]+?)/(?P<creator_id>[^/]+?)/(?P<created_at>[^/]+?)"], endpoint='adminnotes_user_id_creator_id_created_at'),
    dict(resource=Sitedataschemas, urls=[r"/sitedataschemas"], endpoint='sitedataschemas'),
    dict(resource=SitedataschemasSiteId, urls=[r"/sitedataschemas/(?P<site_id>[^/]+?)"], endpoint='sitedataschemas_site_id'),
    dict(resource=Clients, urls=[r"/clients"], endpoint='clients'),
    dict(resource=ClientsClientId, urls=[r"/clients/(?P<client_id>[^/]+?)"], endpoint='clients_client_id'),
    dict(resource=Users, urls=[r"/users"], endpoint='users'),
    dict(resource=UsersUserId, urls=[r"/users/(?P<user_id>[^/]+?)"], endpoint='users_user_id'),
    dict(resource=UsersUserIdActivate, urls=[r"/users/(?P<user_id>[^/]+?)/activate"], endpoint='users_user_id_activate'),
    dict(resource=UsersUserIdDeactivate, urls=[r"/users/(?P<user_id>[^/]+?)/deactivate"], endpoint='users_user_id_deactivate'),
    dict(resource=SitesSiteIdActivate, urls=[r"/sites/(?P<site_id>[^/]+?)/activate"], endpoint='sites_site_id_activate'),
    dict(resource=SitesSiteIdDeactivate, urls=[r"/sites/(?P<site_id>[^/]+?)/deactivate"], endpoint='sites_site_id_deactivate'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass