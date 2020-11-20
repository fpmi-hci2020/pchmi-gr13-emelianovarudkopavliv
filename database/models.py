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

