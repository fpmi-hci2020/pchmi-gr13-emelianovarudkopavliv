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

subscription = api.model('Subscription', {
	'account': fields.String(required=True, description='Email associated with account'),
	'publisher': fields.String(required=True, description='Publisher name')
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

order_entry = api.model('Order entry', {
    'book': fields.Integer(readOnly=True, description='The unique id of a book'),
    'quantity': fields.Integer(required=True, description='How many books')
})

order = api.model('Order', {
	'id': fields.Integer(readOnly=True, description='Unique identifier'),
    'account': fields.String(required=True, description='Account associated with order'),
    'payment_method': fields.String(required=True, description='Payment type: cash or card'),
    'shipping_method': fields.String(required=True, description='Shipping type: deliver or collect'),
    'date_placed': fields.Date(required=True, description='Date on which the order was placed'),
    'date_delivered': fields.Date(required=True, description='Date on which the order was delivered'),
    'price': fields.Float(required=True, description='Total price'),
    'books': fields.List(fields.Nested(order_entry))
})

order_with_books = api.model('Order with books', {
	'id': fields.Integer(readOnly=True, description='Unique identifier'),
    'account': fields.String(required=True, description='Account associated with order'),
    'payment_method': fields.String(required=True, description='Payment type: cash or card'),
    'shipping_method': fields.String(required=True, description='Shipping type: deliver or collect'),
    'date_placed': fields.Date(required=True, description='Date on which the order was placed'),
    'date_delivered': fields.Date(required=True, description='Date on which the order was delivered'),
    'price': fields.Float(required=True, description='Total price'),
    'books': fields.List(fields.Nested(cart))
})
