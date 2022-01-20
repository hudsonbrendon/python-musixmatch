install:
	poetry run python setup.py install

test:
	poetry run pytest tests/tests.py

black:
	poetry run black .

black-check:
	poetry run black . --check

dev:
	make black
	make install
	make test