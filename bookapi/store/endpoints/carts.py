from flask import request, send_file
from flask_restplus import Resource
import io

from bookapi.store.serializers import cart
from bookapi.restplus import api
from database.models import Cart

ns = api.namespace('store/cart', description='Operations related to carts')


@ns.route('/<string:email>')
@api.response(404, 'Account not found')
class CartCollection(Resource):
    
    @api.marshal_with(cart)
    def get(self, email):
        return Cart.query.filter(Cart.account_id == email).all()

