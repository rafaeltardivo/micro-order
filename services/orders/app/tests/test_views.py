from django.test import TestCase
from rest_framework.reverse import reverse


class OrderViewTestCase(TestCase):
    """Test cases for Orders View."""

    def test_orders_create_url(self):
        self.assertEqual(reverse("orders-list"), "/orders/")

    def test_orders_list_url(self):
        self.assertEqual(reverse("orders-list"), "/orders/")

    def test_orders_detail_url(self):
        self.assertEqual(
            reverse("orders-detail", args=[1]), "/orders/1/"
        )
