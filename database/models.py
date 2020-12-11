from datetime import datetime
from database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float)
    availability = db.Column(db.Boolean)

    publisher_name = db.Column(db.String(100), db.ForeignKey('publisher.name'))
    publisher = db.relationship('Publisher', backref=db.backref('books', lazy='dynamic'))

    def __init__(self, title, author, genre, description, price, availability, publisher):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.price = price
        self.availability = availability
        self.publisher = publisher

    def __repr__(self):
        return '<Book %r>' % self.title


class Publisher(db.Model):
    name = db.Column(db.String(100), primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    content = db.Column(db.String(2000))
    date_issued = db.Column(db.Date())

    publisher_name = db.Column(db.String(100), db.ForeignKey('publisher.name'))
    publisher = db.relationship('Publisher', backref=db.backref('news', lazy='dynamic'))

    def __init__(self, title, content, date_issued, publisher):
        self.title = title
        self.content = content
        self.date_issued = date_issued
        self.publisher = publisher

    def __repr__(self):
        return self.title


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    account_id = db.Column(db.String(100), db.ForeignKey('account.email'))
    account = db.relationship('Account', backref=db.backref('subscriptions', lazy='dynamic'))

    publisher_name = db.Column(db.String(100), db.ForeignKey('publisher.name'))
    publisher = db.relationship('Publisher', backref=db.backref('subscriptions', lazy='dynamic'))

    def __init__(self, account, publisher):
        self.account = account
        self.publisher = publisher

    def __repr__(self):
        return self.account_id


class Account(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return self.email


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    cart = db.Column(db.String(10))

    account_id = db.Column(db.String(100), db.ForeignKey('account.email'))
    account = db.relationship('Account', backref=db.backref('cart', lazy='dynamic'))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('carts', lazy='dynamic'))

    def __init__(self, account, book, quantity, cart='cart'):
        self.account = account
        self.book = book
        self.quantity = quantity
        self.cart = cart

    def __repr__(self):
        return '<Cart %r>' % self.account_id


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    account_id = db.Column(db.String(100), db.ForeignKey('account.email'))
    account = db.relationship('Account', backref=db.backref('favorites', lazy='dynamic'))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('favorites', lazy='dynamic'))

    def __init__(self, account, book):
        self.account = account
        self.book = book

    def __repr__(self):
        return '<Favorite %r>' % self.account_id


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(10))
    shipping_method = db.Column(db.String(10))
    date_placed = db.Column(db.Date())
    date_delivered = db.Column(db.Date())
    price = db.Column(db.Float)

    account_id = db.Column(db.String(100), db.ForeignKey('account.email'))
    account = db.relationship('Account', backref=db.backref('orders', lazy='dynamic'))

    def __init__(self, payment_method, shipping_method, account, date_placed=None, date_delivered=None):
        self.payment_method = payment_method
        self.shipping_method = shipping_method
        self.date_placed = datetime.utcnow()
        self.date_delivered = date_delivered
        self.account = account

    def __repr__(self):
        return '<Order %r>' % self.account_id


class BookOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = db.relationship('Order', backref=db.backref('books', lazy='joined'))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('orders', lazy='dynamic'))

    def __init__(self, order, book, quantity):
        self.order = order
        self.book = book
        self.quantity = quantity

    def __repr__(self):
        return '<Book-order %r>' % self.account_id

