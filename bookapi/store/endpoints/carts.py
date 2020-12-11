from flask import request, send_file
from flask_restplus import Resource
import io

from bookapi.store.serializers import cart, cart_entry
from bookapi.store.business import add_to_cart, update_cart, delete_cart_entry
from bookapi.restplus import api
from database.models import Cart

ns = api.namespace('store/cart', description='Operations related to carts')


@ns.route('/')
class CartCollection(Resource):
    
    @api.response(201, 'Book successfully added to cart.')
    @api.expect(cart_entry)
    def post(self):
        data = request.json
        add_to_cart(data)
        return {}, 201

    
    @api.response(204, 'Cart successfully updated.')
    @api.expect(cart_entry)
    def put(self):
        data = request.json
        update_cart(data)
        return {}, 204


@ns.route('/<string:email>')
@api.response(404, 'Account not found')
class CartContents(Resource):
    
    @api.marshal_with(cart)
    def get(self, email):
        return Cart.query.filter(Cart.account_id == email).filter(Cart.cart == 'cart').all()


@ns.route('/<string:email>/<int:book_id>')
@api.response(404, 'Cart entry not found')
class CartContents(Resource):
    
    @api.response(204, 'Cart entry successfully deleted.')
    def delete(self, email, book_id):
        delete_cart_entry(email, book_id)
        return {}, 204

