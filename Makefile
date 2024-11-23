setup:
	curl -sSL https://install.python-poetry.org | python3 - ; \
	pip install --upgrade pip ; \
	pip install poetry keyring keyrings.google-artifactregistry-auth ; \
	poetry config repositories.google https://us-east1-python.pkg.dev/celero-main/celero-finance/

local-install: setup
	poetry install --with dev

lint:
	poetry run black .

test:
	poetry run pytest -s --cov=celero_bfm_fi_proto --cov-report=html -W ignore::DeprecationWarning