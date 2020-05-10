from app.models import Shipping
from django.test import TestCase
from freezegun import freeze_time

from .factories import ShippingFactory


class ShippingsModelTestCase(TestCase):
    """Test cases for Shipping model."""

    def setUp(self):
        with freeze_time('2020-09-05'):
            self.shipping = ShippingFactory()

    def test_create(self):
        self.assertIsInstance(self.shipping, Shipping)

    def test_str(self):
        self.assertEqual(
            str(self.shipping),
            '1 - shipped at 2020-09-05 00:00:00 associated to 1. Status 0'
        )

    def test_repr(self):
        self.assertEqual(
            repr(self.shipping),
            'Shipping(1,1,2020-09-05 00:00:00,0)'
        )
