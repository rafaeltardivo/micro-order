import logging

from decouple import config

from .publishers import Publisher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('orders')

retries = config('CONNECTION_RETRIES', default=3, cast=int)
wait_time = config('SECONDS_BETWEEN_RETRIES', default=2, cast=int)
broker_host = config('BROKER_HOST', default='rabbit')

publisher = Publisher(retries, wait_time, broker_host)
if not publisher.connection:
    logger.info('Could not connect to Broker!')
    raise SystemExit
else:
    logger.info('Successfully connected to broker.')