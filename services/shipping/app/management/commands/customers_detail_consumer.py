from app import consumer
from app.pubsub.callbacks import customers_detail_callback
from decouple import config
from django.core.management.base import BaseCommand

qos = config('PER_WORKER_QOS', default=5, cast=int)


class Command(BaseCommand):
    help = 'Command to start the consumer for orders_create'

    def handle(self, *args, **kwargs):
        exchange = 'customers_detail'
        queue = 'customers_detail_queue'
        routing_key = 'customers_detail'

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
            customers_detail_callback,
        )
        channel.start_consuming()
