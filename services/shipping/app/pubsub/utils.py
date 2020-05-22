import pika
from decouple import config
from retry import retry

retries = config('CONNECTION_RETRIES', default=3, cast=int)
wait_time = config('SECONDS_BETWEEN_RETRIES', default=2, cast=int)


@retry(pika.exceptions.AMQPConnectionError, tries=retries, delay=wait_time)
def get_connection():
    """Create broker connection.
    Args:
        retries (int): Maximum number of retries.
        wait_time (int): Wait time (seconds) between retries.
        broker_host (str): Broker host IP Address or hostname
    Returns:
        pika.BlockingConnection object.
    """
    broker_host = config('BROKER_HOST', default='rabbitmq', cast=str)
    connection = pika.BlockingConnection(
        parameters=pika.ConnectionParameters(
            host=broker_host
        )
    )

    return connection
