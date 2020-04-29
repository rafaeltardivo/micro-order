import os
import pika
import sys

from django.conf import settings

class Producer:
    """Pubsub producer."""
    def __init__(self, host, port,  username, password):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(
                'amqp://{}:{}@{}:{}'.format(username, password, host, port)
            )
        )
        self.channel = self.connection.channel()
        self.exchanges = []

    def produce(self, exchange, payload, routing_key):
        """Produce method."""
        if exchange not in self.exchanges:
            self.channel.exchange_declare(exchange=exchange)
            self.exchanges.append(exchange)

        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=payload
        )
