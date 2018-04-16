"""
This module contains functions that are used to check whether certain calls
are permitted.

Permissions are based on the roles assigned to the user making the request,
which maps to permissions on resources.
"""
import json
import logging
import typing
from uuid import UUID

from aiohttp.web import Request

from management_layer.constants import MKP_ROLE_RESOURCE_PERMISSION, \
    MKP_USER_ROLES, TECH_ADMIN_ROLE_LABEL
from management_layer.mappings import Mappings
from management_layer.settings import CACHE_TIME

# Convenience types
from management_layer.utils import client_exception_handler

logger = logging.getLogger(__name__)

UserId = type(UUID)
SiteId = int
Operator = typing.Callable[..., bool]
Resource = typing.Union[str, int]
Permission = typing.Union[str, int]
ResourcePermission = typing.Tuple[Resource, Permission]
ResourcePermissions = typing.Sequence[ResourcePermission]
Domain = typing.Union[str, int]
Role = typing.Union[str, int]


async def role_has_permission(
    request: Request, role: Role, permission: Permission, resource: Resource,
    nocache: bool = False
) -> bool:
    """
    Check if a role has a specified resource permission.

    Bypassing the cache can have a significant performance impact and should
    only be used in exceptional circumstances.

    :param request: The request associated with this call
    :param role: The role to check
    :param permission: The required permission
    :param resource: The resource
    :param nocache: Bypass the cache if True
    :return: True if the role has the permission on the resource, else False
    """
    result = False
    permission_id = permission if type(permission) is int else \
        Mappings.permission_id_for(permission)

    permission_ids = await get_role_resource_permissions(request, role, resource, nocache=nocache)
    if permission_ids:
        result = permission_id in permission_ids

    return result


async def roles_have_permissions(
    request: Request,
    roles: typing.Set[Role],
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
    :param request: The request associated with this call
    :param roles: A set of role ids
    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param nocache: Bypass the cache if True
    :return: True if the user is has the required permissions on the resources
    """
    if operator not in [all, any]:
        raise RuntimeError("The operator must be all or any")

    # Normalise to ids
    roles = {role if type(role) is int else Mappings.role_id_for(role) for role in roles}

    if Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL) in roles:
        return True

    # This code snippet was originally used before the utility functions were changed
    # into co-routines. It is elegant and efficient and left here for posterity and as
    # an example of the logic that is performed in the code below, which unfortunately
    # ended up being more verbose. - cobusc
    #
    # return operator(
    #     # Any role can provide the permission.
    #     any(role_has_permission(role, permission, resource, nocache) for role in roles)
    #     for resource, permission in resource_permissions)

    for resource, permission in resource_permissions:
        some_role_has_the_permission = False
        for role in roles:
            if await role_has_permission(request, role, permission, resource, nocache=nocache):
                some_role_has_the_permission = True
                break  # No need to look further

        # Short-circuit conditions
        if operator is any and some_role_has_the_permission:
            return True
        if operator is all and not some_role_has_the_permission:
            return False

    # If none of the short-circuit conditions have been met, it means that
    # all of the checks where True if the operator was all, or none of the checks
    # were True if the operator is any.
    return True if operator is all else False


async def user_has_permissions(
    request: Request,
    user: UserId,
    operator: Operator,
    resource_permissions: ResourcePermissions,
    site: SiteId = None,
    domain: Domain = None,
    nocache: bool = False,
) -> bool:
    """
    Check whether the specified user has any or all (as per the operator) of
    the specified resource permissions.
    To establish whether this is the case, we need to interrogate the roles
    associated with the user. If any of the roles has the required
    permission, the requirement is satisfied.
    :param request: The request associated with this call
    :param user: The UUID of the user performing the action
    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param site: The site from which the user is making the request
    :param domain: The domain for which the user is making the request
    :param nocache: Bypass the cache if True
    :return: True if the user is has the required permissions on the resources
    """
    # Either a site or domain needs to be provided, but not both.
    if site is None and domain is None or \
       site is not None and domain is not None:
        raise RuntimeError("Either a site or a domain needs to be provided")

    if operator not in [all, any]:
        raise RuntimeError("The operator must be all or any")

    roles = await get_user_roles_for_site_or_domain(
        request, user, site=site, domain=domain, nocache=nocache
    )
    return await roles_have_permissions(
        request, roles, operator, resource_permissions, nocache=nocache
    )


async def get_user_roles_for_site_or_domain(
    request: Request, user: UserId,
    site: SiteId = None, domain: Domain = None, nocache: bool = False
) -> typing.Set[int]:
    """
    Get the roles assigned to the user for the specified site or domain.
    Either a site or a domain needs to be specified.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param request: The request associated with this call
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
        result = await get_user_roles_for_domain(request, user, domain, nocache=nocache)
    else:
        result = await get_user_roles_for_site(request, user, site, nocache=nocache)

    return result


async def get_role_resource_permissions(
    request: Request, role: Role, resource: Resource, nocache: bool = False
) -> typing.List[int]:
    """
    Get the permission granted on a resource for a specified role.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.

    :param request: The request associated with this call
    :param role: The role
    :param resource: The resource
    :param nocache: Bypass the cache if True
    :return: A list of permission ids
    """
    role_id = role if type(role) is int else Mappings.role_id_for(role)
    resource_id = resource if type(resource) is int else \
        Mappings.resource_id_for(resource)

    key = bytes(f"{MKP_ROLE_RESOURCE_PERMISSION}:{role_id}:{resource_id}",
                encoding="utf8")
    with client_exception_handler():
        role_resource_permissions = None if nocache else await request.app["memcache"].get(key)

    if not role_resource_permissions:
        # The API call returns a List[RoleResourcePermission]
        with client_exception_handler():
            role_resource_permissions = await request.app[
                "access_control_api"].roleresourcepermission_list(
                role_id=role_id, resource_id=resource_id
            )

        # Internally we use only the permission ids, i.e. List[int]
        role_resource_permissions = [
            entry.permission_id for entry in role_resource_permissions
        ]

        with client_exception_handler():
            await request.app["memcache"].set(
                key, json.dumps(role_resource_permissions).encode("utf8"), exptime=CACHE_TIME
            )
    else:
        role_resource_permissions = json.loads(role_resource_permissions, encoding="utf8")

    return role_resource_permissions


async def get_all_user_roles(
    request: Request, user: UserId, nocache: bool = False
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
    :param request: The request associated with this call
    :param user: The user for which to get roles
    :param nocache: Bypass the cache if True
    :return: A dictionary containing the roles assigned to the specified user on
       the domains and sites in the system.
    """
    key = bytes(f"{MKP_USER_ROLES}:{user.hex}", encoding="utf8")
    with client_exception_handler():
        user_roles = None if nocache else await request.app["memcache"].get(key)

    if user_roles is None:
        # The API returns an AllUserRoles object
        with client_exception_handler():
            response = await request.app["operational_api"].get_all_user_roles(user.hex)

        if response.user_id != user.hex:
            raise RuntimeError(f"Invalid API response: {response.user_id} != {user.hex}")
        # We store the roles_map part of the response
        user_roles = response.roles_map
        with client_exception_handler():
            await request.app["memcache"].set(
                key, json.dumps(user_roles).encode("utf8"), exptime=CACHE_TIME)
    else:
        user_roles = json.loads(user_roles, encoding="utf8")

    return user_roles


async def get_user_roles_for_domain(
    request: Request, user: UserId, domain: Domain, nocache: bool = False
) -> typing.Set[int]:
    """
    Get the roles that a user has for a specified domain.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param request: The request associated with this call
    :param user: The user
    :param domain: The site
    :param nocache: Bypass the cache if True
    :return: A set of role ids
    """
    domain_id = domain if type(domain) is int else Mappings.domain_id_for(domain)

    user_roles = await get_all_user_roles(request, user, nocache)
    # Look up the list of role ids associated with the domain key. Return an
    # empty set of it does not exist.
    return set(user_roles.get(f"d:{domain_id}", []))


async def get_user_roles_for_site(
    request: Request, user: UserId, site: SiteId, nocache: bool = False
) -> typing.Set[int]:
    """
    Get the roles that a user has for a specified site.
    Bypassing the cache can have a significant performance and should only be
    used in exceptional circumstances.
    :param request: The request associated with this call
    :param user: The user
    :param site: The site
    :param nocache: Bypass the cache if True
    :return: A set of role ids
    """
    site_id = site if type(site) is int else Mappings.site_id_for(site)

    user_roles = await get_all_user_roles(request, user, nocache)
    # Look up the list of role ids associated with the site key. Return an
    # empty set of it does not exist.
    return set(user_roles.get(f"s:{site_id}", []))
