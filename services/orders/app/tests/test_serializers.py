from app.models import Order
from app.serializers import OrderSerializer
from django.db.models.signals import post_save
from django.test import TestCase
from freezegun import freeze_time

from .factories import OrderFactory


class TestOrderSerializer(TestCase):
    """Test cases for Order serializer."""

    def setUp(self):
        post_save.disconnect(sender=Order, dispatch_uid="post_save_publish")
        with freeze_time('2020-09-05T00:00:00'):
            self.order = OrderFactory()
            self.serializer = OrderSerializer(instance=self.order)

    def test_customer_content(self):
        self.assertEqual(
            self.order.customer,
            self.serializer.data['customer']
        )

    def test_made_at_content(self):
        self.assertEqual(
            str(self.order.made_at),
            self.serializer.data['made_at'])

    def test_status_content(self):
        self.assertEqual(
            Order.STATUS_CHOICES[self.order.status][1],
            self.serializer.data['status']
        )
