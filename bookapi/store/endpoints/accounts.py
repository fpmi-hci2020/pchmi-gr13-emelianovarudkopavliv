from flask import request
from flask_restplus import Resource
from bookapi.store.serializers import account
from bookapi.restplus import api
from database.models import Account

ns = api.namespace('accounts', description='Operations related to user accounts')


@ns.route('/')
class AccountCollection(Resource):

	# POST


@ns.route('/<string:id>')
@api.response(404, 'Account not found')
class AccountItem(Resource):
    
    @api.marshal_with(account)
    def get(self, name):
        return Account.query.filter(Account.name == name).one()
