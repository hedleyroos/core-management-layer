import aiomcache

from management_layer.settings import MEMCACHE_HOST, MEMCACHE_PORT

# The io loop can be passed explicitly to the constructor, if necessary.
memcache = aiomcache.Client(MEMCACHE_HOST, MEMCACHE_PORT)
