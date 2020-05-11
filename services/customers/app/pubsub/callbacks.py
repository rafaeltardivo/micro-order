from app import producer
from app.models import Customer

from . import logger
from .schemas import (customer_detail_schema, customer_request_schema,
                      customer_shipping_schema)


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
    shipping = customer_request_schema().loads(payload)
    logger.info(f'Received shipping customer request payload: {shipping}')
    try:
        customer = Customer.objects.get(id=shipping['customer'])
    except Customer.DoesNotExist:
        logger.info(f"Could not find customer: {shipping['customer']}")
        shipping['customer'] = {}
    else:
        logger.info(f'Retrieved customer: {customer}')
        shipping['customer'] = customer_detail_schema().dump(customer)
    finally:
        shipping_payload = customer_shipping_schema().dumps(shipping)
        producer.publish_to(
            exchange='customers_detail',
            routing_key='customers_detail',
            payload=shipping_payload
        )
