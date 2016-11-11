import os

from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sets import Set
from datetime import datetime

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

columns = Set([column.name for column in Page.__table__.columns.values()])

@app.route('/page/', methods=['POST'])
@cross_origin()
def index():
    """Events endpoint
    """
    data = request.get_json()

    data['sent_at'] = datetime.fromtimestamp(int(data['sent_at'])/1000)

    forwarded_for = request.headers.get('x-forwarded-for')
    if forwarded_for:
        context_ip = forwarded_for.split(',')[0]
    else:
        context_ip = request.remote_addr
    data['context_ip']  = context_ip

    page = Page()
    for key in data:
        if key in columns:
            setattr(page, key, data[key])
    db.session.add(page)
    db.session.commit()
    return ''
