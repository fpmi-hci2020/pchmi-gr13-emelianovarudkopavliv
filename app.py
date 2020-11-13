from bookapi.store.endpoints.books import ns as book_ns
from bookapi.restplus import api
from database import db

from flask import Flask, Blueprint

app = Flask(__name__)

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

def init_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(book_ns)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)

if __name__ == '__main__':
    init_app(app)
    app.run()

