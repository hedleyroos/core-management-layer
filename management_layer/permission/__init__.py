"""
The permission module exposes a decorator that can be used to protect
function calls by specifying the permissions required to execute the function.
"""
import typing
from functools import wraps
from uuid import UUID

from management_layer.permission.utils import Operator, ResourcePermissions, \
    user_has_permissions, Forbidden


def require_permissions(
        operator: Operator,
        resource_permissions: ResourcePermissions,
        nocache: bool = False,
        user_field: typing.Union[int, str] = 0,
        site_field: typing.Union[int, str] = 1
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
