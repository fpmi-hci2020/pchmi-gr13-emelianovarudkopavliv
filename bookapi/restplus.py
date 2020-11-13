from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

api = Api(version=1.0, title='Online bookstore API',
          description='Books, orders and other things for an online bookstore')

@api.errorhandler
def default_error_handler(err):
    message = 'An unhandled exception occured.'
    return {'message': message}, 500

@api.errorhandler(NoResultFound)
def database_not_found_error_handler(err):
    return {'message': 'A database result was required but none was found.'}, 404

