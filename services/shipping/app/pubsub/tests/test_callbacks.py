import json
from unittest.mock import call, patch, Mock

from django.test import TestCase
from freezegun import freeze_time

from ...models import Shipping
from ...tests.factories import ShippingFactory
from ..callbacks import customers_detail_callback, orders_create_callback


class CallbacksTestCase(TestCase):
    """Test cases for Callbacks."""

    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_orders_create_callback(self, mocked_producer, mocked_logger):
        payload = json.dumps({
                'id': 1,
                'customer': 1
            }
        )
        expected_calls = [
            "Received order payload - id:1 customer:1",
            (
                'Created shipping: 1 - shipped at 2020-09-05 00:00:00'
                ' associated to 1. Status 0'
            )
        ]
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'

        with freeze_time('2020-09-05'):
            orders_create_callback(mocked_channel, mocked_method, None, payload)

        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_has_calls([call(item) for item in expected_calls])
        mocked_producer.assert_called_once()
        self.assertTrue(Shipping.objects.count() == 1)
        mocked_channel.basic_ack.assert_called_once()

    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_detail_callback(self, mocked_producer, mocked_logger):
        with freeze_time('2020-09-05'):
            shipping = ShippingFactory()
        payload = json.dumps({
                'id': shipping.pk,
                'customer': {
                    'email': 'someuser@email.com',
                    'address': 'Bucketheadland, number 33'
                }
            }
        )
        expected_calls = [
             (
                f"Received shipping customer detail payload - id:{shipping.pk}"
                f" customer email:someuser@email.com"
                f" customer address:Bucketheadland, number 33"
             ),
             'Customer found. Will set status to SUCCESS'
        ]
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'

        customers_detail_callback(mocked_channel, mocked_method, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_has_calls([call(item) for item in expected_calls])
        mocked_producer.assert_called_once()
        mocked_channel.basic_ack.assert_called_once()

    @patch('app.pubsub.logger.error')
    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_detail_callback_missing_customer(
        self, mocked_producer, mocked_info_logger, mocked_error_log
    ):
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'
        with freeze_time('2020-09-05'):
            shipping = ShippingFactory()
            payload = json.dumps({
                    'id': shipping.pk,
                    'customer': {}
                }
            )
            customers_detail_callback(
                mocked_channel,
                mocked_method,
                None,
                payload
            )
        mocked_info_logger.assert_called_with(
            (
                f"Received shipping customer detail payload - id:{shipping.pk}"
                f" customer email:None"
                f" customer address:None"
             )
        )
        mocked_error_log.assert_called_with(
            'Missing customer. Will set status to FAIL'
        )
        mocked_producer.assert_called_once()
        mocked_channel.basic_ack.assert_called_once()

    @patch('app.pubsub.logger.error')
    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_detail_callback_missing_shipping(
        self, mocked_producer, mocked_info_logger, mocked_error_log
    ):
        payload = json.dumps({
                'id': 99,
                'customer': {}
            }
        )
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'
        customers_detail_callback(mocked_channel, mocked_method, None, payload)
        mocked_info_logger.assert_called_with(
            (
                f"Received shipping customer detail payload - id:99"
                f" customer email:None"
                f" customer address:None"
             )
        )
        mocked_error_log.assert_called_with('Could not find shipping: 99')
        mocked_producer.assert_called_once()
        mocked_channel.basic_ack.assert_called_once()
