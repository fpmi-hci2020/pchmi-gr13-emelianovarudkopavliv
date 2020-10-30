from bookapi import bookapi

import os, signal
from flask import Flask

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s,f: os._exit(0))

@app.route("/")
def get_book():
    page = '<html><body><h1>'
    page += bookapi.get_book()
    page += '</h1></body></html>'
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

