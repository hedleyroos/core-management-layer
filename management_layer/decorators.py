import asyncio
import logging
import typing
from functools import wraps

from kinesis_conducer.producer_events import events, schemas

from management_layer.permission.decorator import get_value_from_args_or_kwargs, \
    get_user_and_site

logger = logging.getLogger(__name__)


def crud_event(
    urn: str,
    action: str,
    request_field: typing.Union[int, str] = 0,
    resource_id_field: typing.Union[int, str] = None,
    body_field: typing.Union[int, str] = None,
    composite_key_fields: typing.Union[str] = None,
) -> typing.Callable:
    """
    This function is used as a decorator for functions that alter resources (CRUD actions,
    without "read").
    These actions are sent to the event log on successful completion.
    ```
    @crud_event("ge:access_control:usersiterole", "create", body_field=1)
    def usersiterole_create(request, body, **kwargs):
        pass

    @crud_event("ge:access_control:usersiterole", "delete", resource_id_field=1)
    def usersiterole_delete(request, usersiterole_id, **kwargs):
        pass
    ```
    The user making the request is inferred from the token passed with the request.

    IMPORTANT: This decorator can be applied to both coroutines and normal functions AND it
    always changes the decorated function into a coroutine, meaning it must be called using `await`:
    ```
    @crud_event("ge:access_control:usersiterole", "create", body_field=1)
    def usersiterole_create(request, body, **kwargs):
        pass

    # Call the function
    result = await usersiterole_create(request, body)  # Decorator change function to coroutine
    ```

    :param urn: The URN of the resource being operated on
    :param action: The action being performed (create, update, delete)
    :param request_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the request parameter.
    :param resource_id_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the resource id field. Note
        that this should only ever be used with "update" and "delete" actions, since the resource
        identifier is only available in the response body of a "create" action.
    :param body_field: An integer or string identifying either the positional
        argument or the name of the keyword argument identifying the body parameter.
    :param composite_key_fields: A list of field names used to construct a composite key for the
        resource. The fields must be available in the body_field and only makes sense
        for "create" actions.
    """
    def wrap(f):
        @wraps(f)
        async def wrapped_f(*args, **kwargs):
            """
            :param args: A list of positional arguments
            :param kwargs: A dictionary of keyword arguments
            :return: Whatever the wrapped function
            """
            # Check that the decorator was implemented correctly.
            if action in ["create", "update"] and body_field is None:
                raise RuntimeError("Action 'create' and 'update' require the body_field "
                                   "argument.")

            if action in ["update", "delete"] and resource_id_field is None:
                raise RuntimeError("Actions 'update' and 'delete' require the "
                                   "resource_id_field argument.")

            if composite_key_fields and action != "create":
                raise RuntimeError("composite_key_fields can only be specified when the "
                                   "action is 'create'.")

            # Extract the request from the function arguments
            request = get_value_from_args_or_kwargs(request_field, args, kwargs)

            user_id, token_site_id = get_user_and_site(request)

            # The decorator needs to get the values for the following variables from the
            # decorated function.
            if body_field is not None:
                body = get_value_from_args_or_kwargs(body_field, args, kwargs)
            else:
                body = dict()

            if asyncio.iscoroutinefunction(f):
                result = await f(*args, **kwargs)
            else:
                result = f(*args, **kwargs)

            # The resource id field can come from the call or, in the case of a create action,
            # the result of the function call.

            if resource_id_field is not None:  # Update and delete actions
                resource_id = get_value_from_args_or_kwargs(resource_id_field, args, kwargs)
            else:  # Create actions
                if composite_key_fields:  # Construct composite key from result field
                    resource_id = get_value_from_args_or_kwargs(composite_key_fields, [], result)
                else:  # Read the id from the response
                    resource_id = result.get("id")  # Get id from response

            # If the call to function f does not raise an exception, then we
            # send the event to the Event Log
            parameters = {
                "event_type": schemas.EventTypes.RESOURCE_CRUD,
                "user_id": user_id.hex,  # The user that made the request
                "site_id": token_site_id,  # The site from which the request came
                "resource_urn": urn,  # The resource name
                "action": action,  # The action performed on the resource
                "resource_id": str(resource_id),  # String representation of the resource id
                "post_action_data": body,
            }
            events.put_event(**parameters)
            logger.debug(f"Event Log: {parameters}")
            return result

        return wrapped_f

    return wrap
