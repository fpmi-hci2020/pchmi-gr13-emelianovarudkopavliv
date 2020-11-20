from flask import request, send_file
from flask_restplus import Resource
from PIL import Image
import io

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


@ns.route('/cover/<int:id>')
@api.response(404, 'Cover image not found')
class BookCover(Resource):
	
	@api.representation('image/png')
	def get(self, id):
		file = io.BytesIO()
		img = Image.new('RGBA', (50, 50), (70, 0, 0, 255))
		img.save(file, 'png')
		file.seek(0)
		return send_file(file,
	                     as_attachment=True,
	                     attachment_filename='annotated.png',
	                     mimetype='image/png')
