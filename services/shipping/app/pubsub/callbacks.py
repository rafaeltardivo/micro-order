from app import producer
from app.models import Shipping

from . import logger
from .schemas import (
    customer_detail_schema,
    customer_request_schema,
    order_create_schema,
    shipping_update_schema,
)


def orders_create_callback(channel, method, properties, payload):
    """Callback for order create events.
    Args:
        channel: Communication channel.
        method: Event method.
        properties: Event properties
        payload (byte): Message payload
    Returns:
        None.
    """

    payload = order_create_schema().loads(payload)
    logger.info(
        (
            f"Received order payload - id:{payload['id']}"
            f" customer:{payload['customer']}"
        )
    )
    shipping = Shipping.objects.create(order=payload['id'])
    logger.info(f'Created shipping: {str(shipping)}')
    shipping_payload = customer_request_schema().dumps(
        {
            'id': shipping.pk,
            'customer': payload['customer']
        }
    )
    producer.publish_to(
        exchange='customers',
        routing_key='customers.request',
        payload=shipping_payload
    )
    channel.basic_ack(delivery_tag=method.delivery_tag)


def customers_detail_callback(channel, method, properties, payload):
    """Callback for customer detail events.
    Args:
        channel: Communication channel.
        method: Event method.
        properties: Event properties
        payload (byte): Message payload
    Returns:
        None.
    """

    payload = customer_detail_schema().loads(payload)
    logger.info(
        (
            f"Received shipping customer detail payload - id:{payload['id']}"
            f" customer email:{payload['customer'].get('email')}"
            f" customer address:{payload['customer'].get('address')}"
        )
    )
    try:
        shipping = Shipping.objects.get(id=payload['id'])
    except Shipping.DoesNotExist:
        logger.error(f"Could not find shipping: {payload['id']}")
        shipping_payload = {}
    else:
        if not len(payload['customer']):
            logger.error(f'Missing customer. Will set status to FAIL')
            shipping.status = Shipping.FAIL
        else:
            logger.info(f'Customer found. Will set status to SUCCESS')
            shipping.status = Shipping.SUCCESS
        shipping.save()
        shipping_payload = shipping_update_schema().dumps(shipping)
    finally:
        producer.publish_to(
            exchange='shippings',
            routing_key='shippings.update',
            payload=shipping_payload
        )
    channel.basic_ack(delivery_tag=method.delivery_tag)
