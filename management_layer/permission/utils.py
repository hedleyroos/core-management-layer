"""
This module contains functions that are used to check whether certain calls
are permitted.

Permissions are based on the roles assigned to the user making the request,
which maps to permissions on resources.
"""
import json
import typing
from uuid import UUID
from functools import wraps
from pymemcache.client.base import PooledClient
from management_layer.access_control.apis.access_control_api import \
    AccessControlApi
from management_layer.access_control.apis.operational_api import OperationalApi

from management_layer.constants import MKP_ROLE_RESOURCE_PERMISSION, \
    MKP_USER_ROLES, TECH_ADMIN, SITES, DOMAINS, ROLES, RESOURCES, \
    PERMISSIONS
from management_layer.settings import CACHE_TIME

# Convenience types
UserId = type(UUID)
SiteId = type(UUID)
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


# TODO: Tweak memcache params
MEMCACHE = PooledClient(("127.0.0.1", 11211),
                        serializer=json_serializer,
                        deserializer=json_deserializer,
                        no_delay=True, connect_timeout=0.5, timeout=1.0)

OA = OperationalApi()
AA = AccessControlApi()

# Name to id mappings. TODO: Populate via API on startup. Move somewhere
# more appropriate.


class Forbidden(Exception):
    """
    An exception raised when a user does not have the required permission(s)
    to perform a function.
    """
    pass


def role_has_permission(
    role: Role, permission: Permission, resource: Resource, nocache: bool=False
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
        PERMISSIONS[permission]

    permission_ids = get_role_resource_permissions(role, resource, nocache)
    if permission_ids:
        result = permission_id in permission_ids

    return result


def roles_have_permissions(
    roles: typing.List[Role],
    operator: Operator,
    resource_permissions: ResourcePermissions,
    nocache: bool=False
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
    site: SiteId=None,
    domain: Domain=None,
    nocache: bool=False
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
    # Either a site or domain needs to be provided
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
    user: UserId, site: SiteId=None, domain: Domain=None, nocache:
        bool=False
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
    # Either a site or domain needs to be provided
    if bool(site) == bool(domain):
        raise RuntimeError("Either a site or a domain needs to be provided")

    if domain:
        result = get_user_roles_for_domain(user, domain, nocache)
    else:
        result = get_user_roles_for_site(user, site, nocache)

    return result


def get_role_resource_permissions(
    role: Role, resource: Resource, nocache: bool=False
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
    role_id = role if type(role) is int else ROLES[role]
    resource_id = resource if type(resource) is int else RESOURCES[resource]

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
    user: UserId, nocache: bool=False
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
    user: UserId, domain: Domain, nocache: bool=False
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
    domain_id = domain if type(domain) is int else DOMAINS[domain]

    user_roles = get_all_user_roles(user, nocache)
    # Look up the list of role ids associated with the domain key. Return an
    # empty list of it does not exist.
    return user_roles.get("d:{}".format(domain_id), [])


def get_user_roles_for_site(
    user: UserId, site: SiteId, nocache: bool=False
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
    site_id = site if type(site) is int else SITES[site]

    user_roles = get_all_user_roles(user, nocache)
    # Look up the list of role ids associated with the site key. Return an
    # empty list of it does not exist.
    return user_roles.get("s:{}".format(site_id), [])


def require_permissions(
    operator: Operator,
    resource_permissions: ResourcePermissions,
    nocache: bool=False,
    user_field: typing.Union[int, str]=0,
    site_field: typing.Union[int, str]=1
) -> typing.Callable:
    """
    This function is used as a decorator to protect functions by specifying
    the permissions that a user requires to perform the action, e.g.
    ```
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    @require_permissions(any, [("urn:ge:test:foo", "read"),
                               ("urn:ge:test:bar", "read"])
    def doSomething(user, site, arg1, arg2):
        pass
    ```
    As can be seen from the example above, the decorator can be stacked.
    Note, however, that for performance reasons the least amount of
    decorators is preferred.
    ```
    # Logically correct, but suboptimal performance
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    @require_permissions(all, [("urn:ge:test:bar", "write")])
    @require_permissions(all, [("urn:ge:test:baz", "write")])
    def badExample(user, site, arg1, arg2):
        pass

    # Logically equivalent to the decorators of example above and more efficient
    @require_permissions(all, [("urn:ge:test:foo", "write"),
                               ("urn:ge:test:bar", "write"),
                               ("urn:ge:test:baz", "write")])
    def goodExample(user, site, arg1, arg2):
        pass
    ```
    This function requires the the user who made the request as well as the
    site from which the request originated in order to look up roles
    associated with the user. The user and site UUID values is picked from
    the values passed to the decorated function. By default we use the first
    argument as the user value and the second as the site. This can be
    changed in the decorator, e.g.
    ```
    @require_permissions(all, [("urn:ge:test:baz", "write")],
                         site_field=2, user_field=3)
    def example1(arg1, arg2, site, user):
        pass

    @require_permissions(all, [("urn:ge:test:baz", "write")],
                         site_field=0, user_field="user")  # "user" in kwargs
    def example2(site, **kwargs):
        pass
    ```

    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param nocache: Bypass the cache if True
    :param user_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the user
        making the request.
    :param site_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the site from
        which the request is made.
    :raises: Forbidden if the user does not have the required permissions.
    """
    if operator not in [any, all]:
        raise RuntimeError("The operator must be any or all")

    def wrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            """
            The purpose of the wrapper is to get the
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Extract the user UUID from the function arguments
            user_field_type = type(user_field)
            if user_field_type is int:
                user = args[user_field]
            elif user_field_type is str:
                user = kwargs[user_field]
            else:
                raise RuntimeError("Invalid value for user_field")

            # Validate the UUID
            if not isinstance(user, UUID):
                raise RuntimeError("User is expected to be a UUID")

            # Extract the site UUID from the function arguments
            site_field_type = type(site_field)
            if site_field_type is int:
                site = args[site_field]
            elif site_field_type is str:
                site = kwargs[site_field]
            else:
                raise RuntimeError("Invalid value for site_field")

            # Validate the UUID
            if not isinstance(site, UUID):
                raise RuntimeError("Site is expected to be a UUID")

            if user_has_permissions(user, operator, resource_permissions,
                                    site=site, nocache=nocache):
                return f(*args, **kwargs)

            # If the necessary permissions are not available, we always raise
            # an exception.
            raise Forbidden()

        return wrapped_f

    return wrap
