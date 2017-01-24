import os
from datetime import datetime

from flask import Flask, json, request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from raven.contrib.flask import Sentry


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": os.environ.get('RELOAD_ORIGINS', '*')}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
sentry = Sentry(app)

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

columns = {column.name for column in Page.__table__.columns.values()}

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

@app.route('/api/30day_active_users', methods=['GET'])
def users():
    if request.args.get('date'):
        date = datetime.strptime(request.args.get('date'), '%Y-%m-%d')
        result = db.engine.execute("""
            select distinct user_id
            from page
            where received_at > '%s'
                and user_id is not null and user_id != ''
            """ % date.strftime('%Y-%m-%d'))
    else:
        result = db.engine.execute("""
            select distinct user_id
            from page
            where received_at > now() - interval '30 days'
                and user_id is not null and user_id != ''
            """)
    return json.jsonify({'user_ids': [int(user_id) for user_id, in result]})
