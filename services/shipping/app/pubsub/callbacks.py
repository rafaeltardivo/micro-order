from app import consumer, logger, producer
from app.models import Shipping


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

    order = consumer.order_create_schema().loads(payload)
    logger.info("Received order Payload: {}".format(order))
    new_shipping = Shipping.objects.create(order=order['id'])

    shipping_payload = producer.customer_request_schema().dumps(
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
        shipping_customer = consumer.customer_detail_schema().loads(payload)
        logger.info("Received shipping customer Payload: {}".format(
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
            shipping.status = Shipping.SUCESS
            shipping.save()
            shipping_payload = producer.shipping_update_schema().dumps(
                shipping
            )
        finally:
            producer.publish_to(
                exchange='shippings_update',
                routing_key='shippings_update',
                payload=shipping_payload
            )
