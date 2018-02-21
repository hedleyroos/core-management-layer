"""
This module contains functions that are used to check whether certain calls
are permitted.

Permissions are based on the roles assigned to the user making the request,
which maps to permissions on resources.
"""
import json
import typing
from uuid import UUID
from pymemcache.client.base import PooledClient

import access_control
from management_layer.constants import MKP_ROLE_RESOURCE_PERMISSION, \
    MKP_USER_ROLES, TECH_ADMIN
from management_layer.mappings import SITE_NAME_TO_ID_MAP, \
    DOMAIN_NAME_TO_ID_MAP, ROLE_LABEL_TO_ID_MAP, RESOURCE_URN_TO_ID_MAP, \
    PERMISSION_NAME_TO_ID_MAP
from management_layer.settings import CACHE_TIME

# Convenience types
UserId = type(UUID)
SiteId = int
Operator = typing.Callable[..., bool]
Resource = typing.Union[str, int]
Permission = typing.Union[str, int]
ResourcePermission = typing.Tuple[Resource, Permission]
ResourcePermissions = typing.Sequence[ResourcePermission]
Domain = typing.Union[str, int]
Role = typing.Union[str, int]


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode('utf-8')
    if flags == 2:
        return json.loads(value.decode('utf-8'))
    raise Exception("Unknown serialization format")


# TODO: Tweak MemCache params
MEMCACHE = PooledClient(("127.0.0.1", 11211),
                        serializer=json_serializer,
                        deserializer=json_deserializer,
                        no_delay=True, connect_timeout=0.5, timeout=1.0)

# TODO: These need to be pulled from a request.app["foo"] !! (cobusc)
OA = access_control.api.OperationalApi()
AA = access_control.api.AccessControlApi()


class Forbidden(Exception):
    """
    An exception raised when a user does not have the required permission(s)
    to perform a function.
    """
    pass


def role_has_permission(
        role: Role, permission: Permission, resource: Resource,
        nocache: bool = False
) -> bool:
    """
    Check if a role has a specified resource permission.

    Bypassing the cache can have a significant performance impact and should
    only be used in exceptional circumstances.

    :param role: The role to check
    :param permission: The required permission
    :param resource: The resource
    :param nocache: Bypass the cache if True
    :return: True if the role has the permission on the resource, else False
    """
    result = False
    permission_id = permission if type(permission) is int else \
        PERMISSION_NAME_TO_ID_MAP[permission]

    permission_ids = get_role_resource_permissions(role, resource, nocache)
    if permission_ids:
        result = permission_id in permission_ids

    return result


def roles_have_permissions(
        roles: typing.List[Role],
        operator: Operator,
        resource_permissions: ResourcePermissions,
        nocache: bool = False
) -> bool:
    """
    Check whether the specified roles has any or all (as per the operator) of
    the specified resource permissions.
    It is typically used as part of the user_has_permissions() function as the
    following simplified pseudo-code shows:

        user_has_permissions(user, operator, resource_permissions):
            roles = get_user_roles()
            return roles_have_permissions(roles, operator, resource_permissions)

    If any of the roles has the required permission, the requirement is
    satisfied.
    Bypassing the cache can have a significant performance impact and should
    only be used in exceptional circumstances.
    :param roles: A list of role ids
    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param nocache: Bypass the cache if True
    :return: True if the user is has the required permissions on the resources
    """
    if operator not in [all, any]:
        raise RuntimeError("The operator must be all or any")

    if TECH_ADMIN in roles:
        return True

    return operator(
        # Any role can provide the permission.
        any(role_has_permission(role, permission, resource, nocache)
            for role in roles)
        for resource, permission in resource_permissions
    )


def user_has_permissions(
        user: UserId,
        operator: Operator,
        resource_permissions: ResourcePermissions,
        site: SiteId = None,
        domain: Domain = None,
        nocache: bool = False
) -> bool:
    """
    Check whether the specified user has any or all (as per the operator) of
    the specified resource permissions.
    To establish whether this is the case, we need to interrogate the roles
    associated with the user. If any of the roles has the required
    permission, the requirement is satisfied.
    :param user: The UUID of the user performing the action
    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param site: The site from which the user is making the request
    :param domain: The domain for which the user is making the request
    :param nocache: Bypass the cache if True
    :return: True if the user is has the required permissions on the resources
    """
    # Either a site or domain needs to be provided, but not both.
    if bool(site) == bool(domain):
        raise RuntimeError("Either a site or a domain needs to be provided")

    if operator not in [all, any]:
        raise RuntimeError("The operator must be all or any")

    roles = get_user_roles_for_site_or_domain(user, site=site, domain=domain,
                                              nocache=nocache)
    return roles_have_permissions(
        roles, operator, resource_permissions, nocache
    )


def get_user_roles_for_site_or_domain(
        user: UserId, site: SiteId = None, domain: Domain = None, nocache:
        bool = False
) -> typing.List[Role]:
    """
    Get the roles assigned to the user for the specified site or domain.
    Either a site or a domain needs to be specified.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param user: The user
    :param site: The site
    :param domain: The domain
    :param nocache: Bypass the cache if True
    :return: A list of roles ids
    """
    # Either a site or domain needs to be provided, but not both.
    if bool(site) == bool(domain):
        raise RuntimeError("Either a site or a domain needs to be provided")

    if domain:
        result = get_user_roles_for_domain(user, domain, nocache)
    else:
        result = get_user_roles_for_site(user, site, nocache)

    return result


def get_role_resource_permissions(
        role: Role, resource: Resource, nocache: bool = False
) -> typing.List[int]:
    """
    Get the permission granted on a resource for a specified role.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.

    :param role: The role
    :param resource: The resource
    :param nocache: Bypass the cache if True
    :return: A list of permission ids
    """
    role_id = role if type(role) is int else ROLE_LABEL_TO_ID_MAP[role]
    resource_id = resource if type(resource) is int else \
        RESOURCE_URN_TO_ID_MAP[resource]

    key = "{}:{}:{}".format(MKP_ROLE_RESOURCE_PERMISSION, role_id, resource_id)
    role_resource_permissions = None if nocache else MEMCACHE.get(key)
    if not role_resource_permissions:
        # The API call returns a List[RoleResourcePermission]
        role_resource_permissions = AA.roleresourcepermission_list(
            role_id=role_id, resource_id=resource_id
        )
        # Internally we use only the permission ids, i.e. List[int]
        role_resource_permissions = [
            entry.permission_id for entry in role_resource_permissions
        ]

        MEMCACHE.set(key, role_resource_permissions, expire=CACHE_TIME)

    return role_resource_permissions


def get_all_user_roles(
        user: UserId, nocache: bool = False
) -> typing.Dict[str, typing.List[int]]:
    """
    This function returns all the roles that a user has on all sites and
    domains in the system. The result looks like this:
    ```
    {
      "d:1": [2, 4],
      "d:2": [2, 4, 6],
      "d:9": [2, 4],
      "d:11": [2, 4],
      "d:10": [2, 4],
      "d:3": [2, 4, 6],
      "d:6": [2, 4, 6],
      "d:4": [2, 4, 6],
      "d:5": [2, 3, 4, 6],
      "d:7": [2, 4, 6],
      "d:8": [2, 4, 6],
      "s:1": [2, 4, 5, 6]
    }
    ```
    The dictionary keys consists of a type indicator ("d" for domains and "s"
    for sites) and an id separated by a ":".
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param user: The user for which to get roles
    :param nocache: Bypass the cache if True
    :return: A dictionary containing the roles assigned to the specified user on
       the domains and sites in the system.
    """
    key = "{}:{}".format(MKP_USER_ROLES, user.hex)
    user_roles = None if nocache else MEMCACHE.get(key)
    if not user_roles:
        # The API returns an AllUserRoles object
        response = OA.get_all_user_roles(user.hex)
        if response.user_id != user.hex:
            raise RuntimeError("Invalid API response: {} != {}".format(
                response.user_id, user.hex
            ))
        # We store the roles_map part of the response
        user_roles = response.roles_map
        MEMCACHE.set(key, user_roles, expire=CACHE_TIME)

    return user_roles


def get_user_roles_for_domain(
        user: UserId, domain: Domain, nocache: bool = False
) -> typing.List[int]:
    """
    Get the roles that a user has for a specified domain.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param user: The user
    :param domain: The site
    :param nocache: Bypass the cache if True
    :return: A list of role ids
    """
    domain_id = domain if type(domain) is int else DOMAIN_NAME_TO_ID_MAP[domain]

    user_roles = get_all_user_roles(user, nocache)
    # Look up the list of role ids associated with the domain key. Return an
    # empty list of it does not exist.
    return user_roles.get("d:{}".format(domain_id), [])


def get_user_roles_for_site(
        user: UserId, site: SiteId, nocache: bool = False
) -> typing.List[int]:
    """
    Get the roles that a user has for a specified site.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param user: The user
    :param site: The site
    :param nocache: Bypass the cache if True
    :return: A list of role ids
    """
    site_id = site if type(site) is int else SITE_NAME_TO_ID_MAP[site]

    user_roles = get_all_user_roles(user, nocache)
    # Look up the list of role ids associated with the site key. Return an
    # empty list of it does not exist.
    return user_roles.get("s:{}".format(site_id), [])
