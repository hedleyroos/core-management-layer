import logging
from functools import wraps

from kinesis_conducer.producer_events import events, schemas

logger = logging.getLogger(__name__)


def crud_push_event(action, urn):
    def wrap(func):
        @wraps(func)
        async def _wrapped(*args, **kwargs):
            events.put_event(
                event_type=schemas.EventTypes.RESOURCE_CRUD,
                site_id=0,
                resource_urn=urn,
                resource_id="1",
                action=action,
                user_id="8a50f7bc-fed2-11e8-9c34-0242ac12000c",
                post_action_data={}
            )
            logger.error("*"*20)
            logger.error("Event pushed to queue")
            logger.error("*"*20)
        return _wrapped
    return wrap
