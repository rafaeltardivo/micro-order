import json
from unittest.mock import patch

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
        customers_request_callback(None, None, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_called_with(
            f'Retrieved customer: {str(self.customer)}'
        )
        mocked_producer.assert_called_once()

    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_request_callback_invalid_customer(
        self, mocked_producer, mocked_logger
    ):
        payload = json.dumps({
                'id': 1,
                'customer': self.customer.pk + 99
            }
        )
        customers_request_callback(None, None, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_called_with(
            f'Could not find customer: {self.customer.pk + 99}'
        )
        mocked_producer.assert_called_once()
