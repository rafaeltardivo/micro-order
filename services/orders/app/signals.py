import json

from django.forms.models import model_to_dict
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from . import logger, publisher

@receiver(post_save, sender=Order)
def publish_order(sender, instance, created, **kwargs):
    """Publisher for the saved order."""

    if created:
        payload = model_to_dict(instance)
        publisher.publish_to(
            exchange='orders',
            routing_key='orders_create',
            payload=json.dumps(payload)
        )
        logger.info("Order: {} published. Payload: {}.".format(
                instance.pk,
                payload
            ) 
        )
    else:
        logger.error("Could not publish Order {}!".format(
                instance.pk
            )
        )

