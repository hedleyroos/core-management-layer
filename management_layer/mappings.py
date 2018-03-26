"""
This module manages the common permission-related information in convenient
formats.

In order to prevent repeated API lookups, data can be loaded when the
application is started and refreshed as necessary. We typically store
dictionaries where the key is the id of the entity, and the value is the entity
itself, as well as a dictionary which maps the text identifier of the entity
to its id.
"""
import logging

from typing import Callable, Tuple, List, Dict, TypeVar, Coroutine, Awaitable
from access_control.api.access_control_api import AccessControlApi

logger = logging.getLogger(__name__)

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
SITE_CLIENT_ID_TO_ID_MAP = {
    "management_layer_workaround": 1  # TODO: Remove when properly implemented
}

# Custom convenience type
T = TypeVar("T")


async def _load(
    api_call: Callable[..., Awaitable[List[T]]],
    name_field: str
) -> Tuple[Dict[int, T], Dict[str, int]]:
    """
    Generic function to load permission-related information from the Access
    Control component.

    :param api_call: The API call that returns the needed information
    :param name_field: The name of the field in which the text name can be found
    :return: A tuple containing the an id->entity map, as well as a str->id
        mapping.
    """
    items_by_id = {}
    name_to_id_map = {}
    offset = 0
    items = await api_call(offset=offset)
    while items:
        for item in items:
            items_by_id[item.id] = item
            name_to_id_map[getattr(item, name_field)] = item.id
        # Check if there are more items
        offset += len(items)
        items = await api_call(offset=offset)

    return items_by_id, name_to_id_map


async def refresh_domains(app):
    """Refresh the global domain information"""
    logger.info("Refreshing domains")
    global DOMAINS
    global DOMAIN_NAME_TO_ID_MAP
    DOMAINS, DOMAIN_NAME_TO_ID_MAP = await _load(app["access_control_api"].domain_list, "name")


async def refresh_permissions(app):
    """Refresh the global permission information"""
    logger.info("Refreshing permissions")
    global PERMISSIONS
    global PERMISSION_NAME_TO_ID_MAP
    PERMISSIONS, PERMISSION_NAME_TO_ID_MAP = await _load(app["access_control_api"].permission_list, "name")


async def refresh_resources(app):
    """Refresh the global resources information"""
    logger.info("Refreshing resources")
    global RESOURCES
    global RESOURCE_URN_TO_ID_MAP
    RESOURCES, RESOURCE_URN_TO_ID_MAP = await _load(app["access_control_api"].resource_list, "urn")


async def refresh_roles(app):
    """Refresh the global roles information"""
    logger.info("Refreshing roles")
    global ROLES
    global ROLE_LABEL_TO_ID_MAP
    ROLES, ROLE_LABEL_TO_ID_MAP = await _load(app["access_control_api"].role_list, "label")


async def refresh_sites(app):
    """Refresh the global sites information"""
    logger.info("Refreshing sites")
    global SITES
    global SITE_NAME_TO_ID_MAP
    SITES, SITE_NAME_TO_ID_MAP = await _load(app["access_control_api"].site_list, "name")
    global SITE_CLIENT_ID_TO_ID_MAP
    SITE_CLIENT_ID_TO_ID_MAP = {
        detail["client_id"]: id_ for id_, detail in SITES.items()
    }


async def refresh_all(app):
    """
    Refresh all data mappings
    """
    logger.info("Refreshing all mappings")
    await refresh_domains(app)
    await refresh_permissions(app)
    await refresh_resources(app)
    await refresh_roles(app)
    await refresh_sites(app)
