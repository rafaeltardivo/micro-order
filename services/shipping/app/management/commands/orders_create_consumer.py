from app import consumer
from app.pubsub.callbacks import orders_create_callback
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Command to start the consumer for orders_create'

    def handle(self, *args, **kwargs):
        exchange = 'orders_create'
        queue = 'orders_create_queue'
        routing_key = 'orders_create'

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
            orders_create_callback,
        )
        channel.start_consuming()
