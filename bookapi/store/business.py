from database import db
from database.models import Book, Account, Cart, Favorite, Publisher, Subscription, News, Order, BookOrder

def query_news(email):
    return db.session.query(News).join(Publisher).join(Subscription).filter(Subscription.account_id == email).all()

def create_account(data):
    account = Account(data.get('email'),
                      data.get('password'))
    db.session.add(account)
    db.session.commit()

def create_book(data):
    publisher_name = data.get('publisher')
    publisher = Publisher.query.filter(Publisher.name == publisher_name).one()
    book = Book(data.get('title'), 
    	        data.get('author'), 
    	        data.get('genre'), 
    	        data.get('description'), 
    	        data.get('price'),
                data.get('availability'),
                publisher)
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


def add_to_favorites(data):
    account_id = data.get('account')
    account = Account.query.filter(Account.email == account_id).one()
    book_id = data.get('book')
    book = Book.query.filter(Book.id == book_id).one()
    favorite = Favorite(account, 
                        book)
    db.session.add(favorite)
    db.session.commit()

def remove_from_favorites(account_id, book_id):
    fav = Favorite.query.filter(Favorite.account_id == account_id).filter(Favorite.book_id == book_id).first()
    db.session.delete(fav)
    db.session.commit()


def create_order(data):
    account_id = data.get('account')
    account = Account.query.filter(Account.email == account_id).one()
    payment_type = data.get('payment_method')
    shipping_type = data.get('shipping_method')
    date_placed = data.get('date_placed')
    order = Order(payment_type, shipping_type, date_placed, account)
    db.session.add(order)

    book_list = data.get('books')
    for book_entry in book_list:
        book_id = book_entry['book']
        book = Book.query.filter(Book.id == book_id).one()
        book_order = BookOrder(order, book, book_entry['quantity'])
        db.session.add(book_order)

    db.session.commit()

def delete_order(id):
    order = Order.query.filter(Order.id == id).first()
    db.session.delete(order)
    db.session.commit()
