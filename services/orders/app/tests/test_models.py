from app.models import Order
from django.db.models.signals import post_save
from django.test import TestCase
from freezegun import freeze_time

from .factories import OrderFactory


class OrdersModelTestCase(TestCase):
    """Test cases for Order model."""

    def setUp(self):
        post_save.disconnect(sender=Order, dispatch_uid="post_save_publish")
        with freeze_time('2020-09-05'):
            self.order = OrderFactory()

    def test_create(self):
        self.assertIsInstance(self.order, Order)

    def test_str(self):
        self.assertEqual(
            str(self.order),
            '1 - made at 2020-09-05 00:00:00+00:00 by customer1. Status: 1'
        )

    def test_repr(self):
        self.assertEqual(
            repr(self.order),
            'Order(1,1,2020-09-05 00:00:00+00:00,1)'
        )
