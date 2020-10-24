lint:
	black simio_app && \
	black tests && \
	pylint simio_app

test:
	pytest -vv

install-dev:
	pip install -r requirements-dev.txt

install:
	pip install -r requirements.txt
