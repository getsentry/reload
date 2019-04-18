requirements:
	pip install -r requirements.txt

requirements-test: requirements
	pip install -r requirements-test.txt

dev: requirements-test
	PORT=8080 python ./run.py

docker:
	docker build --pull --rm -t reload .

test:
	python -m pytest

format:
	python -m black .

lint:
	python -m flake8
	python -m black --check .

.PHONY: requirements requirements-test dev docker test format lint
