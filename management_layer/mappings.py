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
value from memcache, but, if the value is not in memcache or it expired, the
API will be queried and the cache updated.

If multiple instances of the management-layer is running, typically only one
will have to refresh memcache, after which the rest will use the cached values.

IMPORTANT: Dictionaries with integer keys that are serialised to JSON will have those keys
converted to strings when cached and those keys need to be transformed back to integers
after reading from the cache.
"""
import json
import logging

from typing import Callable, Tuple, List, Dict, TypeVar, Awaitable

import aiohttp
import aiomcache
import jwt
from aiohttp import web

from management_layer import transformations
from management_layer.constants import TECH_ADMIN_ROLE_LABEL
from management_layer.settings import CACHE_TIME, AUTHENTICATION_SERVICE_JWKS
from management_layer.sentry import sentry
from management_layer.utils import timeit

logger = logging.getLogger(__name__)


class Mappings:
    # Internal copies of definitions. These are mappings of ids to dictionaries.
    _domains = {}  # type: Dict[int, Dict] (refer to transformations.DOMAIN for more detail)
    _permissions = {}  # type: Dict[int, Dict] (refer to transformations.PERMISSION for more detail)
    _resources = {}  # type: Dict[int, Dict] (refer to transformations.RESOURCE for more detail)
    _roles = {}  # type: Dict[int, Dict] (refer to transformations.ROLE for more detail)
    _sites = {}  # type: Dict[int, Dict] (refer to transformations.SITE for more detail)
    _clients = {}  # type: Dict[int, Dict] (refer to transformations.CLIENT for more detail)
    _keys = {}  # type: Dict[str, Dict]  (refer to JWKS documentation)

    # Name/label to id mappings.
    _domain_name_to_id_map = {}  # type: Dict[str, int]
    _permission_name_to_id_map = {}  # type: Dict[str, int]
    _resource_urn_to_id_map = {}  # type: Dict[str, int]
    _role_label_to_id_map = {}  # type: Dict[str, int]
    _site_name_to_id_map = {}  # type: Dict[str, int]
    _client_name_to_id_map = {}  # type: Dict[str, int]
    _token_client_id_to_site_id_map = {}  # type: Dict[str, int]
    _client_id_to_site_id_map = {}  # type: Dict[int, int]

    @classmethod
    def domain_id_for(cls, name: str) -> int:
        try:
            return cls._domain_name_to_id_map[name]
        except KeyError:
            logger.error(f"'{name}' not in {cls._domain_name_to_id_map}")
            raise

    @classmethod
    def domain_name_for(cls, domain_id: int) -> str:
        try:
            return cls._domains[domain_id]["name"]
        except KeyError:
            logger.error(f"'{domain_id}' not in {cls._domains}")
            raise

    @classmethod
    def permission_id_for(cls, name: str) -> int:
        try:
            return cls._permission_name_to_id_map[name]
        except KeyError:
            logger.error(f"'{name}' not in {cls._permission_name_to_id_map}")
            raise

    @classmethod
    def permission_name_for(cls, permission_id: int) -> str:
        try:
            return cls._permissions[permission_id]["name"]
        except KeyError:
            logger.error(f"'{permission_id}' not in {cls._permissions}")
            raise

    @classmethod
    def resource_id_for(cls, urn: str) -> int:
        try:
            return cls._resource_urn_to_id_map[urn]
        except KeyError:
            logger.error(f"'{urn}' not in {cls._resource_urn_to_id_map}")
            raise

    @classmethod
    def resource_urn_for(cls, resource_id: int) -> str:
        try:
            return cls._resources[resource_id]["urn"]
        except KeyError:
            logger.error(f"'{resource_id}' not in {cls._resources}")
            raise

    @classmethod
    def role_id_for(cls, label: str) -> int:
        try:
            return cls._role_label_to_id_map[label]
        except KeyError:
            logger.error(f"'{label}' not in {cls._role_label_to_id_map}")
            raise

    @classmethod
    def role_label_for(cls, role_id: int) -> str:
        try:
            return cls._roles[role_id]["label"]
        except KeyError:
            logger.error(f"'{role_id}' not in {cls._roles}")
            raise

    @classmethod
    def site_id_for(cls, token_client_id: str) -> int:
        """
        Returns the site linked to a client.
        A token has a "client_id" string, which maps to a client with an integer id.
        This integer id is used in the "client_id" field of a site definition. So::

          token_client_id -> client.id -> site.client_id

        :param token_client_id:
        """

        try:
            return cls._token_client_id_to_site_id_map[token_client_id]
        except KeyError:
            logger.error(f"'{token_client_id}' not in {cls._token_client_id_to_site_id_map}")
            raise

    @classmethod
    def site_name_for(cls, site_id: int) -> str:
        try:
            return cls._sites[site_id]["name"]
        except KeyError:
            logger.error(f"'{site_id}' not in {cls._sites}")
            raise

    @classmethod
    def public_key_for(cls, kid: str) -> Dict:
        try:
            return cls._keys[kid]["public_key"]
        except KeyError:
            logger.error(f"'{kid}' not in {cls._keys}")
            raise

    @classmethod
    def all_resource_permissions(cls):
        """
        This function returns a list of Management Portal permissions, which are concatenations
        of the resource URNs and permission names.
        :return:
        """
        return [
            "{}:{}".format(resource, permission)
            for resource in cls._resource_urn_to_id_map
            for permission in cls._permission_name_to_id_map
        ]


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
        # When items_by_id is JSON-encoded to cache, the integer ids are (implicitly) converted to
        # string, because JSON does not support integer keys. We need to convert them back after
        # reading from the cache.
        items_by_id = {int(id_): value for id_, value in items_by_id.items()}
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
        Mappings._domains, Mappings._domain_name_to_id_map = await _load(
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
        Mappings._permissions, Mappings._permission_name_to_id_map = await _load(
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
        Mappings._resources, Mappings._resource_urn_to_id_map = await _load(
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
        Mappings._roles, Mappings._role_label_to_id_map = await _load(
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
        Mappings._sites, Mappings._site_name_to_id_map = await _load(
            app["access_control_api"].site_list, app["memcache"], transformations.SITE,
            bytes(f"{__name__}:sites", encoding="utf8"), "name", nocache
        )

        Mappings._client_id_to_site_id_map = {
            detail["client_id"]: _id for _id, detail in Mappings._sites.items()
            if "client_id" in detail  # Some sites may not have a client linked yet.
        }
    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_clients(app: web.Application, nocache: bool=False):
    """Refresh the client information
    Because this information is linked to site information, the site information needs to be
    loaded before this.
    """
    logger.info("Refreshing clients")
    try:
        Mappings._clients, Mappings._client_name_to_id_map = await _load(
            app["authentication_service_api"].client_list, app["memcache"], transformations.CLIENT,
            bytes(f"{__name__}:clients", encoding="utf8"), "name", nocache
        )

        Mappings._token_client_id_to_site_id_map = {
            detail["client_id"]: Mappings._client_id_to_site_id_map[id_]
            for id_, detail in Mappings._clients.items()
            if id_ in Mappings._client_id_to_site_id_map
        }
    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_keys(app: web.Application, nocache: bool=False):
    """
    The call for retrieving the JSON Web Token Key Set (JWKS) is not exposed by the Authentication
    Service API since it is part of the OIDC Provider Django application. A simple HTTP request
    (as opposed to using a client library) suffices in this case.
    """
    logger.info("Refreshing keys")
    try:
        items_by_id = {}  # type: Dict[int, T]
        key = bytes(f"{__name__}:jwks", encoding="utf8")
        items = None if nocache else await app["memcache"].get(key)
        if items:
            items_by_id = json.loads(items, encoding="utf8")
            logger.debug(f"Loaded {len(items_by_id)} definitions from cache")
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(AUTHENTICATION_SERVICE_JWKS) as response:
                    jwks = await response.json()

            for entry in jwks["keys"]:
                items_by_id[entry["kid"]] = entry

            await app["memcache"].set(key, json.dumps(items_by_id).encode("utf8"),
                                      CACHE_TIME)
            logger.debug(f"Loaded {len(items_by_id)} definitions from the JWKS end-point")

        for k, parameters in items_by_id.items():
            # We compute the public key based on the parameters provided. The public key is not
            # cached in memcache. Only its parameters are.
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(parameters))
            # We store the computed public key along with the parameters
            items_by_id[k]["public_key"] = public_key

        Mappings._keys = items_by_id

    except Exception as e:
        sentry.captureException()
        logger.error(e)


@timeit(TIMING_LOG_LEVEL)
async def refresh_all(app: web.Application, nocache: bool=False):
    """
    Refresh all data mappings
    """
    logger.info("Refreshing all mappings")
    await refresh_keys(app, nocache)
    await refresh_domains(app, nocache)
    await refresh_permissions(app, nocache)
    await refresh_resources(app, nocache)
    await refresh_roles(app, nocache)
    await refresh_sites(app, nocache)
    # Refresh clients after sites, since it references some site-based data.
    await refresh_clients(app, nocache)


async def return_tech_admin_role_for_testing(*args, **kwargs):
    """
    Many of the test functions require the availability of a function that will return a set
    of roles containing the TECH_ADMIN role. This function does exactly that.
    :return: A set containing the TECH_ADMIN role id
    """
    return {Mappings.role_id_for(TECH_ADMIN_ROLE_LABEL)}

