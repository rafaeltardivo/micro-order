import json
from unittest.mock import call, patch, Mock

from django.test import TestCase

from ...tests.factories import CustomerFactory
from ..callbacks import customers_request_callback


class CallbacksTestCase(TestCase):
    """Test cases for Callbacks."""

    def setUp(self):
        self.customer = CustomerFactory()

    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_request_callback(self, mocked_producer, mocked_logger):
        payload = json.dumps({
                'id': 1,
                'customer': self.customer.pk
            }
        )
        expected_calls = [
            (
                f'Received shipping customer request payload'
                f' - id:1 customer:{self.customer.pk}'
            ),
            f'Retrieved customer: {str(self.customer)}'
        ]
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'

        customers_request_callback(mocked_channel, mocked_method, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_has_calls([call(item) for item in expected_calls])
        mocked_producer.assert_called_once()
        mocked_channel.basic_ack.assert_called_once()

    @patch('app.pubsub.logger.error')
    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_request_callback_invalid_customer(
        self, mocked_producer, mocked_info_logger, mocked_error_logger
    ):
        payload = json.dumps({
                'id': 1,
                'customer': self.customer.pk + 99
            }
        )
        mocked_channel = Mock()
        mocked_channel.basic_ack.return_value = 'mocked return'

        mocked_method = Mock()
        mocked_method.delivery_tag.return_value = 'mocked tag'

        customers_request_callback(mocked_channel, mocked_method, None, payload)
        mocked_info_logger.assert_called_with(
            (
                f'Received shipping customer request payload'
                f' - id:1 customer:{self.customer.pk + 99}'
            ),
        )
        mocked_error_logger.assert_called_with(
            f'Could not find customer: {self.customer.pk + 99}'
        )
        mocked_producer.assert_called_once()
