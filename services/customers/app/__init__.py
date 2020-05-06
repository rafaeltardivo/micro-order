import logging

from .pubsub.consumers import Consumer
from .pubsub.producers import Producer
from .pubsub.utils import get_connection

logFormatter = ('TIMESTAMP:%(asctime)s LEVEL:%(levelname)s MSG:%(message)s')
logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger('customers')

broker_host = "rabbitmq"
connection = get_connection(broker_host)

if not connection:
    logger.info('Could not connect to Broker!')
    raise SystemExit
else:
    logger.info('Successfully connected to broker')

consumer = Consumer(connection)
producer = Producer(connection)
producer.declare_exchange('customers_detail')
