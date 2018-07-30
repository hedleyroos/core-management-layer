"""
The permission module exposes a decorator that can be used to protect
function calls by specifying the permissions required to execute the function.
"""
import asyncio
import json
import logging
import typing
import uuid
from functools import wraps

from management_layer.constants import TECH_ADMIN_ROLE_LABEL, PORTAL_CONTEXT_HEADER
from management_layer.exceptions import JSONForbidden, JSONBadRequest
from management_layer.permission.utils import Operator, ResourcePermissions
from management_layer.mappings import Mappings
from management_layer.permission import utils
from management_layer.settings import MANAGEMENT_PORTAL_CLIENT_ID

logger = logging.getLogger(__name__)


def require_permissions(
    operator: Operator,
    resource_permissions: ResourcePermissions,
    nocache: bool = False,
    request_field: typing.Union[int, str] = 0,
    target_user_field: typing.Union[int, str] = None,
    allow_for_management_portal = False
) -> typing.Callable:
    """
    This function is used as a decorator to restrict functions by specifying
    the permissions that a user requires to perform the action, e.g.
    ```
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    @require_permissions(any, [("urn:ge:test:foo", "read"),
                               ("urn:ge:test:bar", "read"])
    def doSomething(request, arg1, arg2):
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
    def badExample(request, arg1, arg2):
        pass

    # Logically equivalent to the decorators of example above and more efficient
    @require_permissions(all, [("urn:ge:test:foo", "write"),
                               ("urn:ge:test:bar", "write"),
                               ("urn:ge:test:baz", "write")])
    def goodExample(request, arg1, arg2):
        pass
    ```
    This function requires the the user who made the request as well as the
    site from which the request originated (or is made on behalf of) in order to
    look up roles associated with the user. The user and site UUID values are read from
    the token associated with the request field passed to the decorated function.
    By default we use  the first argument as the request field. This can be changed in
    the decorator, e.g.
    ```
    @require_permissions(all, [("urn:ge:test:baz", "write")],
                         request_field=2)
    def example1(arg1, arg2, request):
        pass

    @require_permissions(all, [("urn:ge:test:baz", "write")],
                         request_field="request")  # "request" in kwargs
    def example2(arg1, **kwargs):
        pass
    ```

    IMPORTANT: This decorator can be applied to both coroutines and normal functions AND it
    always changes the decorated function into a coroutine, meaning it must be called using `await`:
    ```
    @require_permissions(all, [("urn:ge:test:foo", "write")])
    def doSomething(request):
        pass

    # Call the function
    result = await doSomething(request)  # Decorator change function to coroutine
    ```

    IMPORTANT: When a function call relates to a particular user, the user does not explicitly
    require permissions on that resource for it to be allowed. A user implicitly has access to
    anything directly related to his profile.
    ```
    @require_permissions(all, [("urn:ge:user", "read")], target_user_field=1)
    def read_user_data(request, user_id):
        pass
    ```
    In the example above, if the user specified by the token in the request is the same user
    as the one identified by the function argument "user_id", then the call is allowed.

    IMPORTANT: The Management Portal may make requests on behalf of the other sites.
    To facilitate this, we look at the X-GE-Portal-Context header in the request:
     * If the header is not present, the context to use is the "audience" of the requesting token.
     * If the header is present and the "audience" of the requesting token is not the Management
       Portal, then return Forbidden.
     * If the header is present and the "audience" of the the requesting token is the Management
       Portal, then use the context specified to look up the user's permissions. (If the specified
       context does not exist, return BadRequest).

    IMPORTANT: The Management Portal needs to be able to perform certain calls (list sites and
    domains, for instance) even if the user does not have explicit permissions to do this.
    For API calls like these, use the `allow_for_manangement_portal` flag, e.g.
    ```
    @require_permissions(all, [("urn:ge:access_control:domain", "list")],
                         allow_for_management_portal=True)
    def domain_list(request, **kwargs):
        pass
    ```

    :param operator: any or all
    :param resource_permissions: The resource permissions required
    :param nocache: Bypass the cache if True
    :param request_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the request parameter.
    :param target_user_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the target user parameter.
    :param allow_for_management_portal: A boolean flag indicating whether access is implied when the
        request is made by the management portal
    :raises: Forbidden if the user does not have the required permissions.
    """
    if operator not in [any, all]:
        raise RuntimeError("The operator must be any or all")

    def wrap(f):
        @wraps(f)
        async def wrapped_f(*args, **kwargs):
            """
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Extract the request from the function arguments
            request = _get_value_from_args_or_kwargs(request_field, args, kwargs)

            user_id, site_id = _get_user_and_site(request)

            # Start by checking if we should allow the call if it was made from the
            # Management Portal and whether the call was in fact made by the Management Portal.
            allowed = allow_for_management_portal and \
                      request["token"]["aud"] == MANAGEMENT_PORTAL_CLIENT_ID

            # If the target user field is specified and the target user is the user
            # that is making the request, then we allow the function call.
            if not allowed and target_user_field is not None:
                # For some calls the specified field may be optional
                try:
                    target_user_id = _get_value_from_args_or_kwargs(target_user_field, args, kwargs)
                    # We cast the values to strings when comparing, to that both strings and UUIDs
                    # can be used.
                    allowed = (str(user_id) == str(target_user_id))
                except KeyError:
                    pass

            # Check if it is the Management Portal making the request on behalf of another site.
            if not allowed:
                context = request.headers.get(PORTAL_CONTEXT_HEADER, None)
                if context:
                    # Only the Management Portal is allowed to use this header.
                    if request["token"]["aud"] != MANAGEMENT_PORTAL_CLIENT_ID:
                        raise JSONForbidden(message="Forbidden")

                    try:
                        context_type, context_id = context.split(":")
                        context_id = int(context_id)
                    except ValueError:
                        raise JSONBadRequest(message="Invalid context header value")

                    if context_type == "d":
                        # See if the user has the required permissions on the specified domain
                        allowed = await utils.user_has_permissions(
                            request, user_id, operator, resource_permissions,
                            domain=context_id, nocache=nocache
                        )
                    elif context_type == "s":
                        # See if the user has the required permissions on the specified site
                        allowed = await utils.user_has_permissions(
                            request, user_id, operator, resource_permissions,
                            site=context_id, nocache=nocache
                        )
                    else:
                        raise JSONBadRequest(message="Invalid context header value")

            # Permissions will only be checked if allowed is not already true.
            allowed = allowed or await utils.user_has_permissions(
                request, user_id, operator, resource_permissions,
                site=site_id, nocache=nocache
            )

            if allowed:
                if asyncio.iscoroutinefunction(f):
                    return await f(*args, **kwargs)
                else:
                    return f(*args, **kwargs)

            raise JSONForbidden(message="Forbidden")

        return wrapped_f

    return wrap


def requester_has_role(
    request_field: typing.Union[int, str] = 0,
    body_field: typing.Union[int, str] = None,
    target_user_id_field: typing.Union[int, str] = None,
    target_invitation_id_field: typing.Union[int, str] = None,
    role_id_field: typing.Union[int, str] = None,
    domain_id_field: typing.Union[int, str] = None,
    site_id_field: typing.Union[int, str] = None,
    nocache: bool = False,
) -> typing.Callable:
    """
    This function is used as a decorator to protect functions that add and remove roles on
    domains and sites to users, e.g.
    ```
    @requester_has_role()
    def usersiterole_create(request, body, **kwargs):
        pass
    ```
    The body must contain the user_id of the recipient, the role_id of the role that must be
    assigned and the site_id of the site for which the user will must get the role.
    ```
    @requester_has_role()
    def usersiterole_delete(request, user_id, site_id, role_id, **kwargs):
        pass
    ```
    The user making the request is inferred from the token passed with the request.

    IMPORTANT: This decorator can be applied to both coroutines and normal functions AND it
    always changes the decorated function into a coroutine, meaning it must be called using `await`:
    ```
    @requester_has_role()
    def doSomething(request, body):
        pass

    # Call the function
    result = await doSomething(request, body)  # Decorator change function to coroutine
    ```

    :param request_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the request parameter.
    :param body_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the body parameter. The
        body parameter is a dictionary that can contain a user_id, role_id and either a
        site_id or domain_id, depending in the call.
    :param target_user_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the user_id field of the target user,
        i.e. the user for which a role must be set or removed.
    :param target_invitation_id_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the invitation_id field of the
        target invitation, i.e. the invitation for which a role must be set or removed.
    :param role_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the role_id field.
    :param domain_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the domain_id field.
    :param site_id_field: An integer or string identifying either the positional argument
        or the name of the keyword argument identifying the site_id field.
    :param nocache: Bypass the cache if True
    :raises: Forbidden if the user does not have the role that is being invoked or revoked.
    """

    def wrap(f):
        @wraps(f)
        async def wrapped_f(*args, **kwargs):
            """
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Extract the request from the function arguments
            request = _get_value_from_args_or_kwargs(request_field, args, kwargs)

            user_id, token_site_id = _get_user_and_site(request)

            # The decorator need to get the values for the following variables from the
            # decorated function.
            role_id = None
            target_user_id = None
            target_invitation_id = None
            domain_id = None
            site_id = None

            if body_field is not None:
                body = _get_value_from_args_or_kwargs(body_field, args, kwargs)

                # When body_field is specified, the xxx_field arguments must be the names of the
                # fields in the body dictionary or None, in which case the defaults will be used.
                role_id = body[role_id_field or "role_id"]
                target_user_id = body.get(target_user_id_field or "user_id")
                target_invitation_id = body.get(target_invitation_id or "invitation_id")
                # We expect either a domain_id or a site_id to be provided
                domain_id = body.get(domain_id_field or "domain_id")
                site_id = body.get(site_id_field or "site_id")
                if domain_id is None and site_id is None or \
                        domain_id is not None and site_id is not None:
                    raise RuntimeError("Either a domain_id or site_id needs to exist in the body")
            else:
                # If the body_field is not specified, the rest of the arguments are considered to be
                # positional arguments.
                role_id = _get_value_from_args_or_kwargs(role_id_field, args, kwargs)
                if domain_id_field is None and site_id_field is None or \
                        domain_id_field is not None and site_id_field is not None:
                    raise RuntimeError("Either a domain_id_field or site_id_field needs to defined")

                if domain_id_field:
                    domain_id = _get_value_from_args_or_kwargs(domain_id_field, args, kwargs)
                else:
                    site_id = _get_value_from_args_or_kwargs(site_id_field, args, kwargs)

                # Extract the user_id or invitation_id for which a role must be a assigned/revoked
                if target_user_id_field is not None:
                    target_user_id = _get_value_from_args_or_kwargs(
                        target_user_id_field, args, kwargs
                    )
                else:
                    target_invitation_id = _get_value_from_args_or_kwargs(
                        target_invitation_id_field, args, kwargs
                    )

            if domain_id:
                user_roles = await utils.get_user_roles_for_domain(request, user_id, domain_id,
                                                                   nocache)
            else:  # Use site_id
                user_roles = await utils.get_user_roles_for_site(request, user_id, site_id, nocache)

            # If the user roles contains the one we want to assign or Tech Admin, we allow
            # the call to proceed.
            if user_roles.intersection([role_id, Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)]):
                if asyncio.iscoroutinefunction(f):
                    return await f(*args, **kwargs)
                else:
                    return f(*args, **kwargs)

            if target_user_id_field is not None:
                log_message = f"User {user_id} cannot assign role {Mappings.role_label_for(role_id)}" \
                              f" to target user {target_user_id} on "
            else:
                log_message = f"User {user_id} cannot assign role {Mappings.role_label_for(role_id)}" \
                              f" to target invitation {target_invitation_id} on "

            if domain_id:
                log_message += f"domain {Mappings.domain_name_for(domain_id)} "
            else:
                log_message += f"site {Mappings.site_name_for(site_id)} "

            log_message += f"because it does not have the role or {TECH_ADMIN_ROLE_LABEL} itself."

            logger.debug(log_message)

            raise JSONForbidden(message=log_message)

        return wrapped_f

    return wrap


def _get_value_from_args_or_kwargs(
    argument_identifier: typing.Union[int, str],
    args: typing.Tuple[typing.Any, ...], kwargs: dict,
):
    """
    :param argument_identifier: The index or name of a function argument
    :param args: A list of positional arguments
    :param kwargs: A dictionary of named arguments
    :return: The value of the argument.
    :raise KeyError: if the argument identified by argument_identifier does not exist.
    :raise RuntimeError: if the argument_identifier argument contains an unexpected value.
    """
    argument_identifier_type = type(argument_identifier)
    if argument_identifier_type is int:
        return args[argument_identifier]

    if argument_identifier_type is str:
        return kwargs[argument_identifier]

    raise RuntimeError("Invalid value for argument identifier")


def _get_user_and_site(request):
    """
    A request contains the JWT token payload from which we get
    * the user id from the "sub" (subscriber) field
    * the client id from the "aud" (audience) field
    :param request: An HttpRequest
    :return: A (user_id, site_id) tuple.
    :raises: HTTPForbidden if the token's client id does not map to a site id.
    """
    # Extract the user's UUID from the request
    user_id = uuid.UUID(request["token"]["sub"])
    # Extract the client id from the request
    client_id = request["token"]["aud"]

    try:
        site_id = Mappings.site_id_for(client_id)
    except KeyError:
        raise JSONForbidden(message=f"No site linked to the client '{client_id}'")

    return user_id, site_id
