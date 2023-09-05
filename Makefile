test:
	python -m pytest -v -s -l api/tests

migration upgrade heads:
	alembic upgrade heads
