from database import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    genre = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float)

    def __init__(self, title, author, genre, description, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.price = price

    def __repr__(self):
        return '<Book %r>' % self.title


class Account(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Account %r>' % self.email


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    account_id = db.Column(db.String(100), db.ForeignKey('account.email'))
    account = db.relationship('Account', backref=db.backref('cart', lazy='dynamic'))

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book', backref=db.backref('carts', lazy='dynamic'))

    def __init__(self, account, book, quantity):
        self.account = account
        self.book = book
        self.quantity = quantity

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
