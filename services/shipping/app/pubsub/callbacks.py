import json

# from . import logger

def bind_orders_callback(channel, method, properties, payload):
    """callback for bind_orders command."""
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    order_payload = json.dumps(payload)

    try:
        pass
    except KeyError:
        # logger.info("Failed to parse order")
        pass
    else:
        pass
        


