requirements:
	pip install -r requirements.txt

dev: requirements
	PORT=8080 python ./run.py

docker:
	docker build --rm -t reload .

.PHONY: requirements dev docker
