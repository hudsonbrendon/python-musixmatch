install:
	pipenv run python setup.py install

test:
	pipenv run pytest tests/tests.py

black:
	pipenv run black .

black-check:
	pipenv run black . --check

dev:
	make black
	make install
	make test