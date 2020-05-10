from unittest.mock import patch

from app.models import Order
from django.db.models.signals import post_save
from django.test import TestCase

from .factories import OrderFactory


class TestOrderSignals(TestCase):
    """Test cases for Orders signals."""

    @patch('app.signals.publish_order', autospec=True)
    def test_order_post_save_publish(self, mocked_handler):

        post_save.connect(
            mocked_handler,
            sender=Order,
            dispatch_uid='post_save_publish'
        )
        OrderFactory()

        self.assertTrue(mocked_handler.called)
        self.assertEquals(mocked_handler.call_count, 1)
