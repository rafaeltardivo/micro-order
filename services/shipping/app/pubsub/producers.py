import pika


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
    
    def publish_to(self, exchange, routing_key, payload):
        """Channel Producer."""
        channel = None

        try:
            channel = self.exchanges['exchange']
        except KeyError:
            channel = self.connection.channel()
            channel.exchange_declare(exchange=exchange)
            self.exchanges['exchange'] = channel
        finally:
            channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=payload
            )
