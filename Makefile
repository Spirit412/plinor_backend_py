test:
	python -m pytest -v -s -l api/tests

migration upgrade heads:
	alembic upgrade heads

init env:
	bash "load_env.sh"