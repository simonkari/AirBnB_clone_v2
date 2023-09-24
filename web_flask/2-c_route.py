#!/usr/bin/python3
""" Hello world in flask"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """route index"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """route C"""
    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
