import factory
from app.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    """ Factory for Customer model."""

    class Meta:
        model = Customer

    email = 'someuser@email.com'
    address = 'Bucketheadland, number 33'
