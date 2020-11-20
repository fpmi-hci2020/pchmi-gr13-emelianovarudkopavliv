from database import db
from database.models import Account

def create_account(data):
    email = data.get('email')
    password = data.get('password')

    account = Account(email, password)

    db.session.add(account)
    db.session.commit()
