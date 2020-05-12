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

    payload = shipping_update_schema().loads(payload)
    logger.info(
        (
            f"Received shipping update payload - id:{payload['id']}"
            f" order:{payload['order']} status:{payload['status']}"
        )
    )
    try:
        order = Order.objects.get(id=payload['order'])
    except Order.DoesNotExist:
        logger.error(f"Could not find order: {payload['order']}")
    else:
        logger.info(f'Retrieved order: {order}')
        order.status = payload['status']
        order.save()
        logger.info(f'Updated order: {order.pk}')
