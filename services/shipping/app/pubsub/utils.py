import pika
import time

import decouple


def get_connection(retries, wait_time, broker_host):
    """Broker connection utility."""
    connection = None

    while(retries > 0):
        try:
            connection = pika.BlockingConnection(
                parameters = pika.ConnectionParameters(
                    host=broker_host)
            )
        except pika.exceptions.AMQPConnectionError:
            retries -= 1
            time.sleep(wait_time)
        else:
            break
    return connection
