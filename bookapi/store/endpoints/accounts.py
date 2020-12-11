from flask import request
from flask_restplus import Resource
from bookapi.store.serializers import account, favorite, fav_entry
from bookapi.store.business import create_account, add_to_favorites, remove_from_favorites
from bookapi.restplus import api
from database.models import Account, Favorite

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


@ns.route('/favorites')
class FavoriteCollection(Resource):
    
    @api.response(201, 'Successfully added to favorites.')
    @api.expect(fav_entry)
    def post(self):
        data = request.json
        add_to_favorites(data)
        return {}, 201


@ns.route('/favorites/<string:email>')
@api.response(404, 'Account not found')
class FavoriteItem(Resource):
    
    @api.marshal_with(favorite)
    def get(self, email):
        return Favorite.query.filter(Favorite.account_id == email).all()


@ns.route('/<string:email>/<int:book_id>')
@api.response(404, 'Favorite not found')
class CartContents(Resource):
    
    @api.response(204, 'Successfully removed from favorites.')
    def delete(self, email, book_id):
        remove_from_favorites(email, book_id)
        return {}, 204

