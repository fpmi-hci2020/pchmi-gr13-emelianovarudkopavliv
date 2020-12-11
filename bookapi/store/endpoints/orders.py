from flask import request, send_file
from flask_restplus import Resource
import io

from bookapi.store.serializers import order
from bookapi.store.business import create_order, delete_order
from bookapi.restplus import api
from database.models import Order

ns = api.namespace('store/order', description='Operations related to orders')


@ns.route('/')
class OrderCollection(Resource):
    
    @api.response(201, 'Order successfully added.')
    @api.expect(order)
    def post(self):
        data = request.json
        create_order(data)
        return {}, 201


@ns.route('/<string:email>')
@api.response(404, 'Account not found')
class OrderContents(Resource):
    
    @api.marshal_with(order)
    def get(self, email):
        return Order.query.filter(Order.account_id == email).all()


@ns.route('/<int:id>')
@api.response(404, 'Order not found')
class OrderItem(Resource):
    
    @api.response(204, 'Order successfully deleted.')
    def delete(self, id):
        delete_order(id)
        return {}, 204
