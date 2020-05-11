from app.models import Order

from . import logger
from .schemas import shipping_update_schema


def shippings_update_callback(channel, method, properties, payload):
    """Callback for shipping update events.
    Args:
        channel: Communication channel.
        method: Event method.
        properties: Event properties
        payload (byte): Message payload
    Returns:
        None.
    """

    if payload:
        shipping_payload = shipping_update_schema().loads(payload)
        logger.info("Received shipping update payload: {}".format(
                 shipping_payload
            )
        )
        try:
            order = Order.objects.get(id=shipping_payload['order'])
        except Order.DoesNotExist:
            logger.info("Could not find order: {}".format(
                    shipping_payload['order']
                )
            )
        else:
            order.status = shipping_payload['status']
            order.save()
            logger.info("Successfully updated order: {}".format(
                    order.pk
                )
            )
    else:
        logger.info("Missing shipping_update payload")
