from app import consumer
from app.pubsub.callbacks import shippings_update_callback
from decouple import config
from django.core.management.base import BaseCommand

qos = config('PER_WORKER_QOS', default=5, cast=int)


class Command(BaseCommand):
    help = 'Command to start the consumer for shippings_update'

    def handle(self, *args, **kwargs):
        exchange = 'shippings_update'
        queue = 'shippings_update_queue'
        routing_key = 'shippings_update'

        channel = consumer.connection.channel()
        channel.queue_declare(
            queue=queue,
            durable=True
        )
        channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key,
        )
        channel.basic_qos(
            prefetch_count=qos
        )
        channel.basic_consume(
            queue,
            shippings_update_callback,
        )
        channel.start_consuming()
