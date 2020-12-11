from flask import request
from flask_restplus import Resource
from bookapi.store.serializers import account, cart
from bookapi.store.business import create_account
from bookapi.restplus import api
from database.models import Account

ns = api.namespace('accounts', description='Operations related to user accounts')


@ns.route('/')
class AccountCollection(Resource):

    @api.response(201, 'Account successfully created.')
    @api.expect(account)
    def post(self):
        data = request.json
        create_account(data)
        return {}, 201


@ns.route('/<string:email>')
@api.response(404, 'Account not found')
class AccountItem(Resource):
    
    @api.marshal_with(account)
    def get(self, email):
        return Account.query.filter(Account.email == email).one()

