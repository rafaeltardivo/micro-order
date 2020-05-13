from app import producer
from app.models import Customer

from . import logger
from .schemas import (
    customer_detail_schema,
    customer_request_schema,
    customer_shipping_schema,
)


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
    payload = customer_request_schema().loads(payload)
    logger.info(
        (
            f'Received shipping customer request payload'
            f" - id:{payload['id']} customer:{payload['customer']}"
        )
    )
    try:
        customer = Customer.objects.get(id=payload['customer'])
    except Customer.DoesNotExist:
        logger.error(f"Could not find customer: {payload['customer']}")
        payload['customer'] = {}
    else:
        logger.info(f'Retrieved customer: {customer}')
        payload['customer'] = customer_detail_schema().dump(customer)
    finally:
        shipping_payload = customer_shipping_schema().dumps(payload)
        producer.publish_to(
            exchange='customers_detail',
            routing_key='customers_detail',
            payload=shipping_payload
        )
    channel.basic_ack(delivery_tag=method.delivery_tag)
