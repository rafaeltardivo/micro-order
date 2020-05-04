from app import consumer
from app.pubsub.callbacks import customers_request_callback
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Command to start the consumer for customers'

    def handle(self, *args, **kwargs):
        exchange = 'customers_request'
        queue = 'customers_request_queue'
        routing_key = 'customers_request'

        channel = consumer.connection.channel()
        channel.queue_declare(
            queue=queue,
            exclusive=True
        )
        channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key,
        )
        channel.basic_consume(
            queue,
            customers_request_callback,
        )
        channel.start_consuming()
