from flask import request, send_file
from flask import request, send_file
from flask_restplus import Resource
import io

from bookapi.store.serializers import book
from bookapi.store.business import create_book
from bookapi.restplus import api
from database.models import Book

ns = api.namespace('store/books', description='Operations related to books')


@ns.route('/')
class BookCollection(Resource):
	
    @api.marshal_list_with(book)
    def get(self):
        books = Book.query.all()
        return books

    @api.response(201, 'Book successfully added to store.')
    @api.expect(book)
    def post(self):
        data = request.json
        create_book(data)
        return {}, 201


@ns.route('/<int:id>')
@api.response(404, 'Book not found')
class BookItem(Resource):
    
    @api.marshal_with(book)
    def get(self, id):
        return Book.query.filter(Book.id == id).one()


@ns.route('/cover/<int:id>')
@api.response(404, 'Cover image not found')
class BookCover(Resource):
	
	@api.representation('image/png')
	def get(self, id):
		with open('src/img/%i.png' % id, 'rb') as f:
			file = io.BytesIO(f.read())
		return send_file(file,
	                     as_attachment=True,
	                     attachment_filename='annotated.png',
	                     mimetype='image/png')
