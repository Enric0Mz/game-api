.PHONY: format run-dev test lint

RUN := poetry run

format:
	@echo "Running black"
	@${RUN} black src tests

	@echo "Running isort"
	@${RUN} isort src tests

	@echo "Running autoflake"
	@${RUN} autoflake --remove-all-unused-imports --remove-unused-variables --remove-duplicate-keys --expand-star-imports -ir src tests

run-dev:
	@CONFIG_ENV=local ${RUN} uvicorn --host 127.0.0.1 --port 5000 src.main:app --reload

run-as-prod:
	@gunicorn --worker-class uvicorn.workers.UvicornWorker -e CONFIG_ENV=prd --bind 0.0.0.0:8000 --name game-api --log-level=info src.main:app

test:
	@CONFIG_ENV=local ${RUN} pytest tests

