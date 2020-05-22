import sys

from loguru import logger

from .pubsub.consumers import Consumer
from .pubsub.producers import Producer
from .pubsub.utils import get_connection

logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time}</green> <blue>{level}</blue> {message}",
)

connection = get_connection()

if not connection:
    logger.info('Could not connect to Broker!')
    raise SystemExit
else:
    logger.info('Successfully connected to broker')

consumer = Consumer(connection)
producer = Producer(connection)
producer.declare_exchange('orders')
producer.declare_exchange('shippings')
producer.declare_exchange('customers')
