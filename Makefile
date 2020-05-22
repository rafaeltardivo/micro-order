build:
	docker-compose build --no-cache
up:
	docker-compose up -d
workers:
	docker-compose exec -d orders su -c "cd services/orders && python manage.py shippings_update_consumer"
	docker-compose exec -d shippings su -c "cd services/shipping && python manage.py customers_detail_consumer"
	docker-compose exec -d shippings su -c "cd services/shipping && python manage.py orders_create_consumer"
	docker-compose exec -d customers su -c "cd services/customers && python manage.py customers_request_consumer"
test:
	docker-compose exec orders su -c "cd services/orders && python manage.py test -v2"
	docker-compose exec shippings su -c "cd services/shipping && python manage.py test -v2"
	docker-compose exec customers su -c "cd services/customers && python manage.py test -v2"
destroy:
	docker-compose down -v
