from flask import request
from flask_restplus import Resource
from bookapi.store.serializers import book
from bookapi.restplus import api
from database.models import Book

ns = api.namespace('store/books', description='Operations related to books')


@ns.route('/')
class BookCollection(Resource):
	
    @api.marshal_list_with(book)
    def get(self):
        books = Book.query.all()
        return books


@ns.route('/<int:id>')
@api.response(404, 'Book not found')
class BookItem(Resource):
    
    @api.marshal_with(book)
    def get(self, id):
        return Book.query.filter(Book.id == id).one()
