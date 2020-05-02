import pika

from . import logger

class Producer:
    __instance = None

    @staticmethod 
    def get_instance(connection):
        """Static access method."""

        if Producer.__instance == None:
            Producer(connection)
            return Producer.__instance

    def __init__(self, connection):
        """Virtually private constructor."""

        if Producer.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            Producer.__instance = self
            Producer.__instance.connection = connection
            Producer.__instance.exchanges = dict()

    def declare_exchange(self, exchange):
        """Declare and store exchange."""

        try:
            channel = self.exchanges[exchange]
            logger.info('Found exchange {}'.format(exchange))
        except KeyError:
            channel = self.connection.channel()
            channel.exchange_declare(exchange=exchange)
            self.exchanges[exchange] = channel
            logger.info('Created exchange {}'.format(exchange))

    def publish_to(self, exchange, routing_key, payload):
        """Exchange Producer."""

        try:
            channel = self.exchanges[exchange]
        except KeyError:
            logger.info('Could not publish to {}'.format(exchange))
        finally:
            channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=payload
            )
            logger.info('Published {} to {}'.format(payload, exchange))

