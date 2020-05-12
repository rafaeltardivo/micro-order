import json
from unittest.mock import patch

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
        with freeze_time('2020-09-05'):
            orders_create_callback(None, None, None, payload)

        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_called_with(
            (
                'Created shipping: 1 - shipped at 2020-09-05 00:00:00'
                ' associated to 1. Status 0'
            )
        )
        mocked_producer.assert_called_once()
        self.assertTrue(Shipping.objects.count() == 1)

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
        customers_detail_callback(None, None, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_called_with(
            'Customer found. Will set status to SUCCESS'
        )
        mocked_producer.assert_called_once()

    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def test_customers_detail_callback_missing_customer(
        self, mocked_producer, mocked_logger
    ):
        with freeze_time('2020-09-05'):
            shipping = ShippingFactory()

        payload = json.dumps({
                'id': shipping.pk,
                'customer': {}
            }
        )
        customers_detail_callback(None, None, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_called_with(
            'Missing customer. Will set status to FAIL'
        )
        mocked_producer.assert_called_once()

    @patch('app.pubsub.logger.info')
    @patch('app.producer.publish_to', return_value=None)
    def customers_detail_callback_missing_shipping(
        self, mocked_producer, mocked_logger
    ):
        payload = json.dumps({
                'id': 99,
                'customer': {}
            }
        )
        customers_detail_callback(None, None, None, payload)
        self.assertEqual(mocked_logger.call_count, 2)
        mocked_logger.assert_called_with(
            'Could not find shipping: 99'
        )
