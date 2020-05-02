import json

from django.forms.models import model_to_dict
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from . import logger, producer

@receiver(post_save, sender=Order)
def publish_order(sender, instance, created, **kwargs):
    """Publisher for the saved order."""

    if created:
        payload = model_to_dict(instance)
        producer.publish_to(
            exchange='orders',
            routing_key='orders_create',
            payload=json.dumps(payload)
        )
    else:
        logger.error("Error creating Order {}!".format(
                instance.pk
            )
        )

