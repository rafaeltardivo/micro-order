# Welcome to micro-order!

A microservice based order system.

## Workflow

0 - An order is created with status `PROCESSING`;

1 - Order `post_save` signal will push the just saved order payload to `orders_create` queue;  
2 - `orders_create_consumer` will consume the order payload from `orders_create` and create a new `Shipping` object. The customer id will be pushed to `customers_request` queue;  
3 - `customers_request_consumer` will consume the customer id   payload from `customers_request` queue, query the customer and push its information payload to `customers_detail` queue;  
4 - `customers_detail_consumer` will consume the customer information from `customers_detail` queue and update the associated `Shipping` object status to `SUCCESS`. Then it will push the updated shipping payload to `shippings_update` queue;  
5 - Finally, `shippings_update_consumer` will consume the updated shipping payload from `shippings_update` queue and set the associated order status to `SHIPPED`.