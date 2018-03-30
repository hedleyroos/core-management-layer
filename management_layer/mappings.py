"""
This module manages the common permission-related information in convenient
formats.

In order to prevent repeated API lookups, data can be loaded when the
application is started and refreshed as necessary. We typically store
dictionaries where the key is the id of the entity, and the value is the entity
itself, as well as a dictionary which maps the text identifier of the entity
to its id.

While the use of shared variables to store these values can be problematic in the case
where an application is multi-threaded, the same is not true when the application
uses an event loop, since it is single-threaded in nature.

The values stored in the mapping class are refreshed when a scheduled
job calls one of the refresh_* functions. Typically a refresh will use a cached
value from Memcache, but, if the value is not in memcache or it expired, the
API will be queried and the cache updated.

If multiple instances of the management-layer is running, typically only one
will have to refresh memcache, after which the rest will use the cached values.

"""
import json
import logging

from typing import Callable, Tuple, List, Dict, TypeVar, Awaitable

import aiomcache
from aiohttp import web

from management_layer import transformations
from management_layer.settings import CACHE_TIME
from management_layer.sentry import sentry
from management_layer.utils import timeit

logger = logging.getLogger(__name__)


class Mappings:
    # Internal copies of definitions. These are mappings of ids to dictionaries.
    domains = {}  # type: Dict[int, Dict]
    permissions = {}  # type: Dict[int, Dict]
    resources = {}  # type: Dict[int, Dict]
    roles = {}  # type: Dict[int, Dict]
    sites = {}  # type: Dict[int, Dict]

    # Name/label to id mappings.
    domain_name_to_id_map = {}  # type: Dict[str, int]
    permission_name_to_id_map = {}  # type: Dict[str, int]
    resource_urn_to_id_map = {}  # type: Dict[str, int]
    role_label_to_id_map = {}  # type: Dict[str, int]
    site_name_to_id_map = {}  # type: Dict[str, int]
    site_client_id_to_id_map = {}  # type: Dict[str, int]


# Custom convenience type
T = TypeVar("T")

TIMING_LOG_LEVEL = logging.INFO

MAPPING_DATA_LIMIT = 100


async def _load(
    api_call: Callable[..., Awaitable[List[T]]],
    memcache: aiomcache.Client, transform: transformations.Transformation,
    key: bytes, name_field: str, nocache: bool=False
) -> Tuple[Dict[int, T], Dict[str, int]]:
    """
    Generic function to load permission-related information from the cache
    or Access Control component.

    :param api_call: The API call that returns the needed information
    :param memcache: The memcache client to use
    :param transform: The transformation to apply to results
    :param key: The cache key to use
    :param name_field: The name of the field in which the text name can be found
    :param nocache: Optional flag to bypass the cache for reading values
    :return: A tuple containing the an id->entity map, as well as a str->id
        mapping.
    """
    items_by_id = {}  # type: Dict[int, T]
    items = None if nocache else await memcache.get(key)
    if items:
        items_by_id = json.loads(items, encoding="utf8")
        logger.debug(f"Loaded {len(items_by_id)} definitions from cache")
    else:
        offset = 0
        while True:
            items = await api_call(offset=offset, limit=MAPPING_DATA_LIMIT)
            if not items:
                # We got no results back, so we can break.
                break

            for item in items:
                items_by_id[item.id] = transform.apply(item.to_dict())

            if len(items) < MAPPING_DATA_LIMIT:
                # We got less results than we asked for which implies there are no more,
                # so we can break.
                break

            # Call API again with new offset
            offset += MAPPING_DATA_LIMIT

        await memcache.set(key, json.dumps(items_by_id).encode("utf8"), CACHE_TIME)
        logger.debug(f"Loaded {len(items_by_id)} definitions from the API")

    name_to_id_map = {
        item[name_field]: id_ for id_, item in items_by_id.items()
    }  # type: Dict[str, int]

    return items_by_id, name_to_id_map


@timeit(TIMING_LOG_LEVEL)
async def refresh_domains(app: web.Application, nocache: bool=False):
    """Refresh the domain information"""
    logger.info("Refreshing domains")
    try:
        Mappings.domains, Mappings.domain_name_to_id_map = await _load(
            app["access_control_api"].domain_list, app["memcache"], transformations.DOMAIN,
            bytes(f"{__name__}:domains", encoding="utf8"), "name", nocache
        )
    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_permissions(app: web.Application, nocache: bool=False):
    """Refresh the permission information"""
    logger.info("Refreshing permissions")
    try:
        Mappings.permissions, Mappings.permission_name_to_id_map = await _load(
            app["access_control_api"].permission_list, app["memcache"], transformations.PERMISSION,
            bytes(f"{__name__}:permissions", encoding="utf8"), "name", nocache
        )
    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_resources(app: web.Application, nocache: bool=False):
    """Refresh the resources information"""
    logger.info("Refreshing resources")
    try:
        Mappings.resources, Mappings.resource_urn_to_id_map = await _load(
            app["access_control_api"].resource_list, app["memcache"], transformations.RESOURCE,
            bytes(f"{__name__}:resources", encoding="utf8"), "urn", nocache
        )
    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_roles(app: web.Application, nocache: bool=False):
    """Refresh the roles information"""
    logger.info("Refreshing roles")
    try:
        Mappings.roles, Mappings.role_label_to_id_map = await _load(
            app["access_control_api"].role_list, app["memcache"], transformations.ROLE,
            bytes(f"{__name__}:roles", encoding="utf8"), "label", nocache
        )
    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_sites(app: web.Application, nocache: bool=False):
    """Refresh the sites information"""
    logger.info("Refreshing sites")
    try:
        Mappings.sites, Mappings.site_name_to_id_map = await _load(
            app["access_control_api"].site_list, app["memcache"], transformations.SITE,
            bytes(f"{__name__}:sites", encoding="utf8"), "name", nocache
        )
        Mappings.site_client_id_to_id_map = {
            detail["client_id"]: id_ for id_, detail in Mappings.sites.items()
        }
    except Exception as e:
        sentry.captureException()
        logger.error(e)

    Mappings.site_client_id_to_id_map["management_layer_workaround"] = 1  # TODO Workaround for now

# @timeit(TIMING_LOG_LEVEL)
# async def refresh_sites(app: web.Application, nocache: bool=False):
#     """Refresh the sites information"""
#     logger.info("Refreshing sites")
#     try:
#         key = bytes(f"{__name__}:sites", encoding="utf8")
#
#         items = None if nocache else await app["memcache"].get(key)
#         if not items:
#             logger.debug("Loading from API")
#             items_by_id = {}  # type: Dict[int, T]
#             offset = 0
#             # TODO: Sort out the bug regarding calling the `api_call` more than once
#             limit = 1
#             while True:
#                 successful_api_call = False
#                 while not successful_api_call:
#                     try:
#                         items = await app["access_control_api"].site_list(offset=offset, limit=limit)
#                         successful_api_call = True
#                     except Exception as e:
#                         logger.error(str(e))
#
#                 if items:
#                     for item in items:
#                         items_by_id[item.id] = transformations.SITE.apply(item.to_dict())
#                     # Check if there are more items
#                     if len(items) < limit:
#                         # We got less than we asked for, so no more to process.
#                         break
#                     else:
#                         offset += limit
#                 else:
#                     break
#             await app["memcache"].set(key, json.dumps(items_by_id).encode("utf8"), CACHE_TIME)
#         else:
#             logger.debug("Loaded from cache")
#             items_by_id = json.loads(items, encoding="utf8")
#
#         name_to_id_map = {
#             item["name"]: id_ for id_, item in items_by_id.items()
#         }  # type: Dict[str, int]
#
#         Mappings.sites = items_by_id
#         Mappings.site_name_to_id_map = name_to_id_map
#         Mappings.site_client_id_to_id_map = {
#             detail["client_id"]: id_ for id_, detail in Mappings.sites.items()
#         }
#         Mappings.site_client_id_to_id_map["management_layer_workaround"] = 1  # TODO Workaround for now
#     except Exception as e:
#         logger.error(str(e))


@timeit(TIMING_LOG_LEVEL)
async def refresh_all(app: web.Application, nocache: bool=False):
    """
    Refresh all data mappings
    """
    logger.info("Refreshing all mappings")
    await refresh_domains(app, nocache)
    await refresh_permissions(app, nocache)
    await refresh_resources(app, nocache)
    await refresh_roles(app, nocache)
    await refresh_sites(app, nocache)
