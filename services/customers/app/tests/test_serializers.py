from app.serializers import CustomerSerializer
from django.test import TestCase

from .factories import CustomerFactory


class TestCustomerSerializer(TestCase):
    """Test cases for Customer serializer."""

    def setUp(self):
        self.customer = CustomerFactory()
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_email_content(self):
        self.assertEqual(self.customer.email, self.serializer.data['email'])

    def test_address_content(self):
        self.assertEqual(
            self.customer.address,
            self.serializer.data['address']
        )
