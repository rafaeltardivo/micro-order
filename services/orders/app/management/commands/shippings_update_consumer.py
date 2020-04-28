from app import consumer
from app.pubsub.callbacks import shippings_update_callback
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Command to start the consumer for shippings_update'

    def handle(self, *args, **kwargs):
        exchange = 'shippings_update'
        queue = 'shippings_update_queue'
        routing_key = 'shippings_update'

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
            shippings_update_callback,
        )
        channel.start_consuming()
