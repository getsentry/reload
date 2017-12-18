requirements:
	pip install -r requirements.txt

requirements-test: requirements
	pip install -r requirements-test.txt

dev: requirements-test
	PORT=8080 python ./run.py

docker:
	docker build --rm -t reload .

.PHONY: requirements requirements-test dev docker
