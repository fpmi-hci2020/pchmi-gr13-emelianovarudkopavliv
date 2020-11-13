from flask_restplus import fields
from bookapi.restplus import api

book = api.model('Book', {
    'id': fields.Integer(readOnly=True, description='The unique id of a book'),
    'title': fields.String(required=True, description='Book title'),
    'author': fields.String(required=True, description='Book author'),
    'genre': fields.String(description='Book genre'),
    'description': fields.String(description='Book description or synopsis'),
    'price': fields.Float(required=True, description='Book price'),
})

