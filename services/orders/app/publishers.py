import time

import pika


class Publisher:
    __instance = None

    @staticmethod 
    def get_instance(retries, wait_time, host):
        """Static access method."""

        if Publisher.__instance == None:
            Publisher(retries, wait_time, host)
            return Publisher.__instance

    def __init__(self, retries, wait_time, host):
        """Virtually private constructor."""
        connection = None

        if Publisher.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            Publisher.__instance = self
            while(retries > 0):
                try:
                    connection = pika.BlockingConnection(
                        parameters = pika.ConnectionParameters(
                            host=host)
                    )
                except pika.exceptions.AMQPConnectionError:
                    retries -= 1
                    time.sleep(wait_time)
                else:
                    break
        Publisher.__instance.connection = connection
        Publisher.__instance.exchanges = dict()
    
    def publish_to(self, exchange, routing_key, payload):
        """Channel publisher."""
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