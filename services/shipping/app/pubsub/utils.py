import time

import pika


def get_connection(retries, wait_time, broker_host):
    """Create broker connection.
    Args:
        retries (int): Maximum number of retries.
        wait_time (int): Wait time (seconds) between retries.
        broker_host (str): Broker host IP Address or hostname
    Returns:
        pika.BlockingConnection object.
    """
    connection = None

    while(retries > 0):
        try:
            connection = pika.BlockingConnection(
                parameters=pika.ConnectionParameters(
                    host=broker_host
                )
            )
        except pika.exceptions.AMQPConnectionError:
            retries -= 1
            time.sleep(wait_time)
        else:
            break
    return connection
