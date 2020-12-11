from database import db
from database.models import Book, Account, Cart

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

def add_to_cart(data):
    account_id = data.get('account')
    account = Account.query.filter(Account.email == account_id).one()
    book_id = data.get('book')
    book = Book.query.filter(Book.id == book_id).one()
    quantity = data.get('quantity')
    cart = Cart(account, 
                book, 
                quantity)
    db.session.add(cart)
    db.session.commit()

def update_cart(data):
    account_id = data.get('account')
    book_id = data.get('book')
    cart_entry = Cart.query.filter(Cart.account_id == account_id).filter(Cart.book_id == book_id).first()
    cart_entry.quantity = data.get('quantity')
    db.session.commit()

def delete_cart_entry(account_id, book_id):
    cart_entry = Cart.query.filter(Cart.account_id == account_id).filter(Cart.book_id == book_id).first()
    db.session.delete(cart_entry)
    db.session.commit()
