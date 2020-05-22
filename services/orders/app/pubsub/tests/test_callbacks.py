import json
from unittest.mock import call, patch, Mock

from django.db.models.signals import post_save
from django.test import TestCase
from freezegun import freeze_time

from ...models import Order
from ...tests.factories import OrderFactory
from ..callbacks import shippings_update_callback


class CallbacksTestCase(TestCase):
    """Test cases for Callbacks."""

    def setUp(self):
        post_save.disconnect(sender=Order, dispatch_uid="post_save_publish")
        with freeze_time('2020-09-05'):
            self.order = OrderFactory()

    @patch('app.pubsub.logger.info')
    def test_shippings_update_callback(self, mocked_logger):
        payload = json.dumps({
                'id': 1,
                'order': self.order.pk,
                'status': 1
            }
        )
        expected_calls = [
            (
                f"Received shipping update payload - id:1"
                f" order:{self.order.pk} status:1"
            ),
            f'Retrieved order: {str(self.order)}',
            f'Updated order: {self.order.pk}'
        ]
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'

        shippings_update_callback(mocked_channel, mocked_method, None, payload)
        self.assertEqual(mocked_logger.call_count, 3)
        mocked_logger.assert_has_calls([call(item) for item in expected_calls])
        mocked_channel.basic_ack.assert_called_once()

    @patch('app.pubsub.logger.error')
    @patch('app.pubsub.logger.info')
    def test_shippings_update_callback_invalid_order(
        self, mocked_info_logger, mocked_error_logger
    ):
        payload = json.dumps({
                'id': 1,
                'order': self.order.pk + 99,
                'status': 1
            }
        )
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'

        shippings_update_callback(mocked_channel, mocked_method, None, payload)
        mocked_info_logger.assert_called_with(
            (
                f"Received shipping update payload - id:1"
                f" order:{self.order.pk + 99} status:1"
            )
        )
        mocked_error_logger.assert_called_with(
            f'Could not find order: {self.order.pk + 99}'
        )
        mocked_channel.basic_ack.assert_called_once()