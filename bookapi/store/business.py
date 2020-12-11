from database import db
from database.models import Book

def create_account(data):
    account = Account(data.get('email'),
                      data.get('password'))
    db.session.add(account)
    db.session.commit()

def create_book(data):
    book = Book(data.get('title'), 
    	        data.get('author'), 
    	        data.get('genre'), 
    	        data.get('description'), 
    	        data.get('price'))
    db.session.add(book)
    db.session.commit()
