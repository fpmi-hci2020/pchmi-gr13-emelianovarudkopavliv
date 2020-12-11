from flask_restplus import fields
from bookapi.restplus import api

book = api.model('Book', {
    'id': fields.Integer(readOnly=True, description='The unique id of a book'),
    'title': fields.String(required=True, description='Book title'),
    'author': fields.String(required=True, description='Book author'),
    'genre': fields.String(description='Book genre'),
    'description': fields.String(description='Book description or synopsis'),
    'price': fields.Float(required=True, description='Book price'),
    'publisher': fields.String(required=True, description='Publisher'),
    'availability': fields.Boolean(required=True, description='If the book is available')
})

account = api.model('Account', {
    'email': fields.String(required=True, description='Email associated with account'),
    'password': fields.String(required=True, description='Account password'),
})

cart = api.model('Cart', {
    'book': fields.Nested(book),
    'quantity': fields.Integer(required=True, description='How many books')
})

cart_entry = api.inherit('Cart entry', {
    'account': fields.String(required=True, description='Email associated with account'),
    'book': fields.Integer(readOnly=True, description='The unique id of a book'),
    'quantity': fields.Integer(required=True, description='How many books')
})

favorite = api.model('Favorite', { 
	'book': fields.Nested(book) 
})

fav_entry = api.inherit('Favorite entry', {
    'account': fields.String(required=True, description='Email associated with account'),
    'book': fields.Integer(readOnly=True, description='The unique id of a book')
})

news = api.model('News', { 
	'title': fields.String(required=True, description='News title'),
	'content': fields.String(required=True, description='News content'), 
	'date_issued': fields.Date(required=True, description='Date of issue'),
	'publisher': fields.String(description='Publisher'),
})

