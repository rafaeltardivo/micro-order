import os
import pika

class Consumer:
    """Pubsub consumer."""
    def __init__(self, host, port, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def _init_channel(self):
        """Channel creation method."""
        self.connection = pika.BlockingConnection(
            pika.URLParameters(
                'amqp://{}:{}@{}:{}'.format(
                    self.username,
                    self.password,
                    self.host,
                    self.port
                )
            )
        )
        self.channel = self.connection.channel()
        return self.channel

    def _init_queue(self, exchange, queue_name, routing_key):
        """Queue creation method."""
        self.channel.queue_declare(queue=queue_name)
        result = self.channel.queue_bind(
            exchange=exchange, 
            queue=queue_name,
            routing_key=routing_key
        )
        return result.method.queue

    def consume(self, exchange, queue_name, routing_key, callback):
        """Consume method."""
        channel = self._init_channel()
        queue_name = self._init_queue(exchange, queue_name, routing_key)
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
        )

