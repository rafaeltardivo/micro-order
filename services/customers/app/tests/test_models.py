from app.models import Customer
from django.test import TestCase

from .factories import CustomerFactory


class CustomersModelTestCase(TestCase):
    """Test cases for Customer model."""

    def setUp(self):
        self.customer = CustomerFactory()

    def test_create(self):
        self.assertIsInstance(self.customer, Customer)

    def test_str(self):
        self.assertEqual(
            str(self.customer),
            '1 - someuser@mail.com who lives at Bucketheadland, number 33'
        )

    def test_repr(self):
        self.assertIs(
            repr(self.customer),
            'Customer(1,someuser@mail.com,Bucketheadland, number 33'
        )
