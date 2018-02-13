"""
This module manages the common permission-related information in convenient
formats.

In order to prevent repeated API lookups, data can be loaded when the
application is started and refreshed as necessary. We typically store
dictionaries where the key is the id of the entity, and the value is the entity
itself, as well as a dictionary which maps the text identifier of the entity
to its id.
"""
from typing import Callable, Tuple, List, Dict, TypeVar
from access_control.api.access_control_api import AccessControlApi

# Internal copies of definitions
DOMAINS = {}
PERMISSIONS = {}
RESOURCES = {}
ROLES = {}
SITES = {}

# Name/label to id mappings
DOMAIN_NAME_TO_ID_MAP = {}
PERMISSION_NAME_TO_ID_MAP = {}
RESOURCE_URN_TO_ID_MAP = {}
ROLE_LABEL_TO_ID_MAP = {}
SITE_NAME_TO_ID_MAP = {}

# The API client used to load the data
API = AccessControlApi()

# Custom convenience type
T = TypeVar("T")


def _load(
    api_call: Callable[..., List[T]],
    name_field: str
) -> Tuple[Dict[int, T], Dict[str, int]]:
    """
    Generic function to load permission-related information from the Access
    Control component.

    TODO: We may have to use the asynchronous variants of the API calls.

    :param api_call: The API call that returns the needed information
    :param name_field: The name of the field in which the text name can be found
    :return: A tuple containing the an id->entity map, as well as a str->id
        mapping.
    """
    items_by_id = {}
    name_to_id_map = {}
    offset = 0
    items = api_call(offset=offset)
    while items:
        for item in items:
            items_by_id[item.id] = item
            name_to_id_map[getattr(item, name_field)] = item.id
        # Check if there are more items
        offset += len(items)
        items = api_call(offset=offset)

    return items_by_id, name_to_id_map


def refresh_domains():
    """Refresh the global domain information"""
    global DOMAINS
    global DOMAIN_NAME_TO_ID_MAP
    DOMAINS, DOMAIN_NAME_TO_ID_MAP = _load(API.domain_list, "name")


def refresh_permissions():
    """Refresh the global permission information"""
    global PERMISSIONS
    global PERMISSION_NAME_TO_ID_MAP
    PERMISSIONS, PERMISSION_NAME_TO_ID_MAP = _load(API.permission_list, "name")


def refresh_resources():
    """Refresh the global resources information"""
    global RESOURCES
    global RESOURCE_URN_TO_ID_MAP
    RESOURCES, RESOURCE_URN_TO_ID_MAP = _load(API.resource_list, "urn")


def refresh_roles():
    """Refresh the global roles information"""
    global ROLES
    global ROLE_LABEL_TO_ID_MAP
    ROLES, ROLE_LABEL_TO_ID_MAP = _load(API.role_list, "label")


def refresh_sites():
    """Refresh the global sites information"""
    global SITES
    global SITE_NAME_TO_ID_MAP
    SITES, SITE_NAME_TO_ID_MAP = _load(API.site_list, "name")


def refresh_all():
    """
    Refresh all data mappings
    """
    refresh_domains()
    refresh_permissions()
    refresh_resources()
    refresh_roles()
    refresh_sites()
