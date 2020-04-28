from app import consumer, logger, producer
from app.models import Customer


def customers_request_callback(channel, method, properties, payload):
    """Callback for customer request events.
    Args:
        channel: Communication channel.
        method: Event method.
        properties: Event properties
        payload (byte): Message payload
    Returns:
        None.
    """

    shipping = consumer.customer_request_schema().loads(payload)
    logger.info("Received shipping customer Payload: {}.".format(shipping))
    try:
        customer = Customer.objects.get(id=shipping['customer'])
    except Customer.DoesNotExist:
        shipping_payload = None
    else:
        shipping['customer'] = producer.customer_detail_schema().dump(customer)
        shipping_payload = producer.customer_shipping_schema().dumps(shipping)
    finally:
        producer.publish_to(
            exchange='customers_detail',
            routing_key='customers_detail',
            payload=shipping_payload
        )
