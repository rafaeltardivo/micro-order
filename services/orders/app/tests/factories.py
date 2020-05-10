import factory
from app.models import Order


class OrderFactory(factory.django.DjangoModelFactory):
    """ Factory for Order model."""

    class Meta:
        model = Order

    customer = 1
    status = Order.PROCESSING
