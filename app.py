import os
from time import time

import boto3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sync(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	created = db.Column(db.DateTime, default=func.now())
	updated = db.Column(db.DateTime, onupdate=func.now())
	completed = db.Column(db.Boolean, default=False)
	local = db.Column(db.Text)

	def upload_to_s3(self):
		with open(self.local, 'r') as data:
			boto3.resource('s3').Bucket(os.environ['S3_BUCKET']).put_object(Key=str(self.id), Body=data)
			# TODO delete local file

	def copy_to_redshift(self):
		with psycopg2.connect(
			host=os.environ['REDSHIFT_HOST'],
			port=os.environ['REDSHIFT_PORT'],
			database=os.environ['REDSHIFT_DATABASE'],
			user=os.environ['REDSHIFT_USER'],
			password=os.environ['REDSHIFT_PW']) as conn:
			with conn.cursor() as curs:
				sql = "copy %s from 's3://%s/%s' credentials \
					'aws_access_key_id=%s;aws_secret_access_key=%s'" % (
					Page.__tablename__,
					os.environ['S3_BUCKET'],
					self.id,
					os.environ['AWS_ACCESS_KEY_ID'],
					os.environ['AWS_SECRET_ACCESS_KEY'])
				curs.execute(sql)
				# TODO delete s3 object
				self.completed = True

	def with_redshift(self):
		self.upload_to_s3()
		self.copy_to_redshift()
		self.completed = True
		db.session.add(self)
		db.session.commit()


class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	received_at = db.Column(db.DateTime, default=func.now())

	anonymous_id = db.Column(db.String(128))
	user_id = db.Column(db.Integer)
	sent_at = db.Column(db.DateTime)
	url = db.Column(db.Text)

	path = db.Column(db.Text)
	search = db.Column(db.Text)
	campaign_source = db.Column(db.Text)
	campaign_name = db.Column(db.Text)
	campaign_term = db.Column(db.Text)
	campaign_medium = db.Column(db.Text)
	user_agent = db.Column(db.Text)
	referrer = db.Column(db.Text)
	ip = db.Column(db.Text)
	title = db.Column(db.Text)

	@classmethod
	def prep_for_sync(cls):
		fpath = '/tmp/%d.csv' % int(time())
		with open(fpath, 'w') as f:
			with psycopg2.connect(
				database=os.environ['PG_DATABASE'],
				user=os.environ['PG_USER']) as conn:

				with conn.cursor() as curs:
					curs.copy_to(f, cls.__tablename__, sep=',')
					curs.execute("DELETE FROM %s;" % cls.__tablename__)

		sync = Sync()
		sync.local = fpath
		db.session.add(sync)
		db.session.commit()
		return sync


@app.route('/page', methods=['POST'])
def index():
	"""Events endpoint
	"""
	return ''


def sync():
	"""Sync to redshift"""
	Page.prep_for_sync()
	syncs = Sync.query.filter_by(completed=False).all()
	for sync in syncs:
		sync.with_redshift()
		db.session.add(sync)
	db.session.commit()
