# micro-order
An  (asynchronous, pubsub-based and microservice oriented) order app.

## Technology
 - Docker
 - Docker Compose
 - Django 3.0.0
 - Django REST Framework 3.10.0
 - Marshmallow 3.5.2
 - Pika 1.1.0
 - Python Decouple 3.3.0

## How to run

1 - Build:
```
docker-compose build --no-cache
```

2 - Run:
```
docker-compose up
```

## Services  

|  Service |  Port |
|---|---|
| orders  | :8000  |
| shippings  |  :8001 |
|  customers |  :8002 |

The broker (rabbitmq) will run on port 5672.

## Consumers (workers)  
|  Worker | Description  |
|---|---|
|  customers_request_consumer | handles customer detail requests  |
|  shippings_update_consumer | handles shipping status updates  |
|  customers_detail_consumer | handles customer detail responses  |
|   orders_create_consumer |  handles order creation events |

## Workflow

1 - Customer creation
```
curl --request POST \
  --url http://localhost:8002/customers/ \
  --header 'content-type: application/json' \
  --data '{
	"email": "user@email.com",
	"address": "Moutain View, 33"
}'
```

2 - Order creation (using the customer id)
```
curl --request POST \
  --url localhost:8000/orders/ \
  --header 'content-type: application/json' \
  --data '{
	"customer": <<CUSTOMER_ID>>
}'
```

### Events description

0 - An order is created with status `PROCESSING`;  

1 - Order `post_save` signal will push the just saved order payload to `orders_create` queue;  
2 - `orders_create_consumer` will consume the order payload from `orders_create` and create a new `Shipping` object. The customer id will be pushed to `customers_request` queue;  
3 - `customers_request_consumer` will consume the customer id   payload from `customers_request` queue, query the customer and push its information payload to `customers_detail` queue.  
4 - `customers_detail_consumer` will consume the customer information from `customers_detail` queue and update the associated `Shipping` object status to `SUCCESS`. Then it will push the updated shipping payload to `shippings_update` queue;  
5 - Finally, `shippings_update_consumer` will consume the updated shipping payload from `shippings_update` queue and set the associated order status to `SHIPPED`.
