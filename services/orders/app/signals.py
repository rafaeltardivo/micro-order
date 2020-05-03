from django.db.models.signals import post_save
from django.dispatch import receiver

from . import logger, producer
from .models import Order
from .pubsub.schemas import OrderProducerSchema


@receiver(post_save, sender=Order)
def publish_order(sender, instance, created, **kwargs):
    """Publisher for the saved order.
        Args:
            sender (Order): Model class.
            instance (Order): Actual instance being saved.
            created (Boolean): True if a new record was created.
            **kwargs: Keyworded variable length argument list.
        Returns:
            None.
    """

    if created:
        logger.info("Created order: {}".format(instance.pk))
        payload = OrderProducerSchema().dumps(instance)
        producer.publish_to(
            exchange="orders", routing_key="orders_create", payload=payload
        )
    else:
        logger.info("Updated order: {}".format(instance.pk))
