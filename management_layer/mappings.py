from typing import Callable, Tuple, List, Dict, TypeVar
from management_layer.access_control.apis.access_control_api import \
    AccessControlApi as AC

# Name/label to id mappings
DOMAIN_NAME_TO_ID_MAP = {}
PERMISSION_NAME_TO_ID_MAP = {}
RESOURCE_URN_TO_ID_MAP = {}
ROLE_LABEL_TO_ID_MAP = {}
SITE_NAME_TO_ID_MAP = {}

# Internal copies of definitions
DOMAINS = {}
PERMISSIONS = {}
RESOURCES = {}
ROLES = {}
SITES = {}

# The API client
API = AC()

T = TypeVar(T)
def load(
    api_call: Callable[..., List[T]],
    name_field: str
) -> Tuple[Dict[]]
    """

    :param api_call:
    :param name_field:
    :return:
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
    global DOMAINS
    global DOMAIN_NAME_TO_ID_MAP
    DOMAINS, DOMAIN_NAME_TO_ID_MAP = load(API.domain_list, "name")


def refresh_permissions():
    global PERMISSIONS
    global PERMISSION_NAME_TO_ID_MAP
    PERMISSIONS, PERMISSION_NAME_TO_ID_MAP = load(API.permission_list, "name")


def refresh_resources():
    global RESOURCES
    global RESOURCE_URN_TO_ID_MAP
    RESOURCES, RESOURCE_URN_TO_ID_MAP = load(API.resource_list, "urn")


def refresh_roles():
    global ROLES
    global ROLE_LABEL_TO_ID_MAP
    ROLES, ROLE_LABEL_TO_ID_MAP = load(API.role_list, "label")


def refresh_sites():
    global SITES
    global SITE_NAME_TO_ID_MAP
    SITES, SITE_NAME_TO_ID_MAP = load(API.site_list, "name")


def refresh_all():
    refresh_domains()
    refresh_permissions()
    refresh_resources()
    refresh_roles()
    refresh_sites()


refresh_all()

