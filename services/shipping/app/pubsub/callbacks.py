import json

from app import logger, producer

from app.models import Shipping

def bind_orders_callback(channel, method, properties, payload):
    """callback for bind_orders command."""    

    try:
        order = json.loads(payload)
        customer = order['customer']
        order_id = order['id']
    except (TypeError, KeyError):
        logger.info("Could not parse payload: {}.".format(payload))
    else:
        logger.info("Received order Payload: {}.".format(order))
        new_shipping = Shipping.objects.create(order=order_id)
        
        payload = {
            'shipping': new_shipping.pk,
            'customer': customer
        }

        producer.publish_to(
            exchange='shippings',
            routing_key='shippings_create',
            payload=json.dumps(payload)
        )


