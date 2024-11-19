setup:
	curl -sSL https://install.python-poetry.org | python3 - ; \
	pip install --upgrade pip ; \
	pip install poetry keyring keyrings.google-artifactregistry-auth ; \
	poetry config repositories.google https://us-east1-python.pkg.dev/celero-main/celero-finance/

local-install: setup
	poetry install --extras keycloak --with dev

lint:
	poetry run flake8

test:
	poetry run pytest -s --cov=celero_idp --cov-report=html -W ignore::DeprecationWarning