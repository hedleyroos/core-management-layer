from functools import partial
from raven import Client
from raven_aiohttp import QueuedAioHttpTransport

from management_layer.settings import SENTRY_DSN

sentry = Client(
    dsn=SENTRY_DSN,
    transport=partial(QueuedAioHttpTransport, workers=5, qsize=1000)
)