from bookapi import bookapi

import os, signal
from flask import Flask, jsonify

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s,f: os._exit(0))

@app.route("/books/book", methods=['GET'])
def get_book():
    book = bookapi.get_book()
    return jsonify(book)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

