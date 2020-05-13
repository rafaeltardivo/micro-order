# micro-order

An (asynchronous, pubsub-based and microservice oriented) order app.

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

1) Build: `make build`
2) Run services: `make up`
3) Run workers: `make workers`

## Services

|  Service  |  Port  |
|-----------|--------|
| orders    | `8000` |
| shippings | `8001` |
| customers | `8002` |

### Observations

- The broker (`rabbitmq`) will run over the port 5672;
- Each service will create a small [sqlite](https://www.sqlite.org/).

## Consumers (workers)

|            Worker          |            Description            |
|----------------------------|-----------------------------------|
| customers_request_consumer | handles customer detail requests  |
| shippings_update_consumer  | handles shipping status updates   |
| customers_detail_consumer  | handles customer detail responses |
| orders_create_consumer     | handles order creation events     |

## Workflow

1) Customer creation
```
curl --request POST \
  --url http://localhost:8002/customers/ \
  --header 'content-type: application/json' \
  --data '{
  "email": "user@email.com",
  "address": "Moutain View, 33"
}'
```

2) Order creation (using the customer id)
```
curl --request POST \
  --url localhost:8000/orders/ \
  --header 'content-type: application/json' \
  --data '{
  "customer": <<CUSTOMER_ID>>
}'
```

Then, all other actions are async ;)

## API Doc

[http://localhost:9000](http://localhost:9000)

## Contributing guidelines

### Using pre-commit

pre-commit is a tools that helps us commiting better code.

More information at: https://pre-commit.com/

1) Install pre-commit following this guide: https://pre-commit.com/#installation
2) Install the hooks on your project: In your local repository, run: `pre-commit install`
3) Test if it's working fine running `pre-commit run`
