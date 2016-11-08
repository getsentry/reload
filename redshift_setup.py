import os

import psycopg2
from sqlalchemy.schema import CreateTable

from app import Page

with psycopg2.connect(
	host=os.environ['REDSHIFT_HOST'],
	port=os.environ['REDSHIFT_PORT'],
	database=os.environ['REDSHIFT_DATABASE'],
	user=os.environ['REDSHIFT_USER'],
	password=os.environ['REDSHIFT_PW']) as conn:
	with conn.cursor() as curs:
		curs.execute(CreateTable(Page.__table__).__str__())