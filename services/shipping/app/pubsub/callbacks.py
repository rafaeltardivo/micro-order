from app import producer
from app.models import Shipping

from . import logger
from .schemas import (customer_detail_schema, customer_request_schema,
                      order_create_schema, shipping_update_schema)


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

    order_payload = order_create_schema().loads(payload)
    logger.info(f'Received order payload: {order_payload}')
    shipping = Shipping.objects.create(order=order_payload['id'])
    logger.info(f'Created shipping: {shipping}')

    shipping_payload = customer_request_schema().dumps(
        {
            'id': shipping.pk,
            'customer': order_payload['customer']
        }
    )
    producer.publish_to(
        exchange='customers_request',
        routing_key='customers_request',
        payload=shipping_payload
    )


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

    shipping_customer = customer_detail_schema().loads(payload)
    logger.info(
        f'Received shipping customer detail payload: {shipping_customer}'
    )
    try:
        shipping = Shipping.objects.get(id=shipping_customer['id'])
    except Shipping.DoesNotExist:
        logger.info(f"Could not find shipping: {shipping_customer['id']}")
        shipping_payload = {}
    else:
        if not len(shipping_customer['customer']):
            logger.info(f'Missing customer. Will set status to FAIL')
            shipping.status = Shipping.FAIL
        else:
            logger.info(f'Customer found. Will set status to SUCCESS')
            shipping.status = Shipping.SUCCESS
        shipping.save()
        shipping_payload = shipping_update_schema().dumps(shipping)
    finally:
        producer.publish_to(
            exchange='shippings_update',
            routing_key='shippings_update',
            payload=shipping_payload
        )
