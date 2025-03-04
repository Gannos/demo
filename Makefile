build:
	docker-compose up -d --build

rebuild:
	docker-compose down -v
	docker-compose up --build --force-recreate

stop:
	docker-compose down

logs:
	docker-compose logs -f
