requirements:
	pip install -r requirements.txt

dev: requirements
	python ./run.py

docker:
	docker build --rm -t reload .

.PHONY: requirements dev docker
