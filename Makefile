bootstrap:
	createdb -E UTF-8 reload
	source .env; ./redshift_setup.py

develop:
	pip install -r requirements.txt
	source .env; python -c "from app import db; db.create_all()"

dev:
	export FLASK_DEBUG=1
	export FLASK_APP=app.py
	source .env
	flask run