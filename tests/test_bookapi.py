from bookapi import bookapi

def test_get_book():
    assert bookapi.get_book() == 'Hello world!'
