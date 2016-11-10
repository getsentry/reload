import os
from time import time

import boto3
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import psycopg2

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    received_at = db.Column(db.DateTime, default=func.now())
    sent_at = db.Column(db.DateTime)
    url = db.Column(db.Text)
    referrer = db.Column(db.Text)
    title = db.Column(db.Text)
    path = db.Column(db.Text)
    search = db.Column(db.Text)

    anonymous_id = db.Column(db.String(128))
    user_id = db.Column(db.Text)

    context_ip = db.Column(db.Text)
    context_user_agent = db.Column(db.Text)
    context_campaign_source = db.Column(db.Text)
    context_campaign_name = db.Column(db.Text)
    context_campaign_term = db.Column(db.Text)
    context_campaign_medium = db.Column(db.Text)
    context_campaign_content = db.Column(db.Text)
    context_user_agent = db.Column(db.Text)

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


@app.route('/api/page/', methods=['POST'])
@cross_origin()
def index():
    """Events endpoint
    """
    data = request.get_json()
    data['context_ip'] = request.headers.get('x-forwarded-for') or request.remote_addr

    page = Page()
    for key in data:
        if key in [column.name for column in Page.__table__.columns.values()]:
            setattr(page, column.name, data[column.name])
    db.session.add(page)
    db.session.commit()
    return ''
