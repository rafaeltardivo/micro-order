from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app import consumer
from app.pubsub.callbacks import bind_orders_callback

class Command(BaseCommand):
    help = 'Command to start the consumer for orders'

    def add_arguments(self, parser):
        parser.add_argument('exchange', type=str, help='Exchange to bind queue')
        parser.add_argument('queue', type=str, help='Queue name')
        parser.add_argument('routing_key', type=str, help='Routing key')

    def handle(self, *args, **kwargs):
        exchange = kwargs['exchange']
        queue = kwargs['queue']
        routing_key = kwargs['routing_key']

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
            bind_orders_callback,
        )
        channel.start_consuming()

