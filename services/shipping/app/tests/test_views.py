from django.test import TestCase
from rest_framework.reverse import reverse


class ShippingViewTestCase(TestCase):
    """Test cases for Shippings View."""

    def test_shippings_create_url(self):
        self.assertEqual(reverse("shippings-list"), "/shippings/")

    def test_shippings_list_url(self):
        self.assertEqual(reverse("shippings-list"), "/shippings/")

    def test_shippings_detail_url(self):
        self.assertEqual(
            reverse("shippings-detail", args=[1]), "/shippings/1/"
        )
