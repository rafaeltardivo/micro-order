import factory
from app.models import Shipping


class ShippingFactory(factory.django.DjangoModelFactory):
    """ Factory for Shipping model."""

    class Meta:
        model = Shipping

    order = 1
    status = Shipping.PROCESSING
