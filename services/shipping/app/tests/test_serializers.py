from app.models import Shipping
from app.serializers import ShippingSerializer
from django.test import TestCase
from freezegun import freeze_time

from .factories import ShippingFactory


class TestShippingSerializer(TestCase):
    """Test cases for Shipping serializer."""

    def setUp(self):
        with freeze_time('2020-09-05T00:00:00'):
            self.shipping = ShippingFactory()
            self.serializer = ShippingSerializer(instance=self.shipping)

    def test_order_content(self):
        self.assertEqual(
            self.shipping.order,
            self.serializer.data['order']
        )

    def test_shipped_at_content(self):
        self.assertEqual(
            str(self.shipping.shipped_at),
            self.serializer.data['shipped_at'])

    def test_status_content(self):
        self.assertEqual(
            Shipping.STATUS_CHOICES[self.shipping.status][1],
            self.serializer.data['status']
        )
