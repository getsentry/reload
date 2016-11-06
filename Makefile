bootstrap:
	mkvirtualenv reload
	createdb -E UTF-8 reload
	./redshift_setup.py

develop:
	pip install -r requirements.txt
	python -c "from app import db; db.create_all()"

dev:
	export FLASK_DEBUG=1
	export FLASK_APP=app.py
	./.env
	flask run