install:
	pipenv run python setup.py install

test:
	pipenv run python tests/tests.py

black:
	pipenv run black .

black-check:
	pipenv run black . --check

dev:
	make black
	make install
	make test