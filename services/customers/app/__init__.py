import logging

from decouple import config

from .pubsub.consumers import Consumer
from .pubsub.producers import Producer
from .pubsub.utils import get_connection

logFormatter = ('TIMESTAMP:%(asctime)s LEVEL:%(levelname)s MSG:%(message)s')
logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger('customers')

retries = config('CONNECTION_RETRIES', default=3, cast=int)
wait_time = config('SECONDS_BETWEEN_RETRIES', default=2, cast=int)
broker_host = config('BROKER_HOST', default="rabbitmq", cast=str)

connection = get_connection(retries, wait_time, broker_host)

if not connection:
    logger.info('Could not connect to Broker!')
    raise SystemExit
else:
    logger.info('Successfully connected to broker')

consumer = Consumer(connection)
producer = Producer(connection)
producer.declare_exchange('customers_detail')
