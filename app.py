from bookapi.store.endpoints.books import ns as book_ns
from bookapi.restplus import api
from database import db

import os, signal
from flask import Flask, Blueprint

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

app = Flask(__name__)

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://torftgqndjevbk:7f45aed3cd2dafd6d6cedc61408e4fdb6fa653a0ffcedd5983965d36e77c6420@ec2-184-73-249-9.compute-1.amazonaws.com:5432/deenv7gf477jaj'

def init_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)

    api.add_namespace(book_ns)
    # api.add_namespace(account_ns)

    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)

if __name__ == '__main__':
    init_app(app)
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

