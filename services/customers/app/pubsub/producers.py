from . import logger


class Producer:
    __instance = None

    @staticmethod
    def get_instance(connection):
        """Static access to Producer singleton.
        Args:
            connection (pika.BlockingConnection): BlockingConnection object.
        Returns:
            Producer singleton.
        """

        if Producer.__instance is None:
            Producer(connection)
            return Producer.__instance

    def __init__(self, connection):
        """Virtually private constructor for Producer singleton.
        Args:
            connection (pika.BlockingConnection): BlockingConnection object.
        """

        if Producer.__instance is not None:
            raise TypeError("This class is a Singleton!")
        else:
            Producer.__instance = self
            Producer.__instance.connection = connection
            Producer.__instance.exchanges = dict()

    def declare_exchange(self, exchange):
        """Declare and store exchange.
        Args:
            exchange (str): Exchange name.
        Returns:
            None.
        """

        try:
            channel = self.exchanges[exchange]
            logger.info('Found exchange {}'.format(exchange))
        except KeyError:
            channel = self.connection.channel()
            channel.exchange_declare(exchange=exchange)
            self.exchanges[exchange] = channel
            logger.info('Created exchange {}'.format(exchange))

    def publish_to(self, exchange, routing_key, payload):
        """Publish payload to exchange.
        Args:
            exchange (str): Exchange name.
            routing_key (str): routing key name for binding.
            payload (json): routing key name for binding.
        Returns:
            None.
        """

        try:
            channel = self.exchanges[exchange]
        except KeyError:
            logger.info('Could not publish to {}'.format(exchange))
        else:
            channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=payload
            )
            logger.info('Published: {} to: {}'.format(payload, exchange))
