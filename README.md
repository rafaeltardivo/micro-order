# micro-order
An  (asynchronous, pubsub-based and microservice oriented) order app.

## Technology
 - [Django](https://www.djangoproject.com/) 3.0
 - [Django REST Framework](https://www.django-rest-framework.org/) 3.10
 - [Docker](https://www.docker.com/) 19.03.06
 - [Docker Compose](https://docs.docker.com/compose/) 1.25.0
 - [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)3.5.2
 - [Pika](https://pika.readthedocs.io/en/stable/) 1.1.0
 - [Python](https://www.python.org/) 3.6.5
 - [Python Decouple](https://github.com/henriquebastos/) 3.3
 - [Rabbit MQ](https://www.rabbitmq.com/) 3.8
 - [Retry](https://pypi.org/project/retry/) 0.9

## How to run

1 - Build:
```
make build
```

2 - Run services:
```
make up
```
2 - Run workers:
```
make workers
```


## Services

|  Service |  Port |
|---|---|
| orders  | `8000`  |
| shippings  |  `8001` |
|  customers |  `8002` |

### Observations
- The broker (`rabbitmq`) will run on port 5672;
 - Each service will create a small [sqlite](https://www.sqlite.org/).

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
3 - `customers_request_consumer` will consume the customer id   payload from `customers_request` queue, query the customer and push its information payload to `customers_detail` queue;
4 - `customers_detail_consumer` will consume the customer information from `customers_detail` queue and update the associated `Shipping` object status to `SUCCESS`. Then it will push the updated shipping payload to `shippings_update` queue;
5 - Finally, `shippings_update_consumer` will consume the updated shipping payload from `shippings_update` queue and set the associated order status to `SHIPPED`.
