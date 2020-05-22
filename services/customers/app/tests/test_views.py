from django.test import TestCase
from rest_framework.reverse import reverse


class CustomerViewTestCase(TestCase):
    """Test cases for Customers View."""

    def test_customers_create_url(self):
        self.assertEqual(reverse("customers-list"), "/customers/")

    def test_customers_list_url(self):
        self.assertEqual(reverse("customers-list"), "/customers/")

    def test_customers_detail_url(self):
        self.assertEqual(
            reverse("customers-detail", args=[1]), "/customers/1/"
        )
