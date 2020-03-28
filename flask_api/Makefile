.PHONY: test coverage

install:
	docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

start:
	docker-compose up server

coverage:
	docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

daemon:
	docker-compose up -d server 

test:
	docker-compose run --rm testserver

lint:
	docker-compose run --rm server bash -c "python -m flake8 ./src ./test"
### DATABASE
# ¯¯¯¯¯¯¯¯
db-run:
	docker run -it --rm --network some-network postgres psql -h some-postgres -U postgres

db/connect:
	docker-compose exec db psql -Upostgres

db/downgrade:
	docker-compose run --rm server python src/manage.py db downgrade

db/upgrade:
	docker-compose run --rm server python src/manage.py db upgrade

db/migrate:
	docker-compose run --rm server python src/manage.py db migrate
### TEST
# ¯¯¯¯¯¯¯¯
test/coverage: ## Generate test coverage
	docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

test/lint: ## Lint python files with flake8
	docker-compose run --rm server bash -c "python -m flake8 ./src ./test"

test/safety: ## Check for dependencies security breach with safety
	docker-compose run --rm server bash -c "python vendor/bin/safety check"
