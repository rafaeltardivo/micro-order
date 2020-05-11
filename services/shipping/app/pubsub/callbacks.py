from app import logger, producer
from app.models import Shipping

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

    order = order_create_schema().loads(payload)
    logger.info("Received order payload: {}".format(order))
    new_shipping = Shipping.objects.create(order=order['id'])

    shipping_payload = customer_request_schema().dumps(
        {
            'id': new_shipping.pk,
            'customer': order['customer']
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

    if payload:
        shipping_customer = customer_detail_schema().loads(payload)
        logger.info("Received shipping customer detail payload: {}".format(
                 shipping_customer
            )
        )

        try:
            shipping = Shipping.objects.get(id=shipping_customer['id'])
        except Shipping.DoesNotExist:
            logger.info("Could not find shipping: {}".format(
                shipping_customer['id']
                )
            )
            shipping_payload = None
        else:
            if not len(shipping_customer['customer']):
                shipping.status = Shipping.FAIL
            else:
                shipping.status = Shipping.SUCCESS
            shipping.save()
            shipping_payload = shipping_update_schema().dumps(
                shipping
            )
        finally:
            producer.publish_to(
                exchange='shippings_update',
                routing_key='shippings_update',
                payload=shipping_payload
            )
