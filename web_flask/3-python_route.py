#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, request

app = Flask(__name__)  # The Flask application instance
app.url_map.strict_slashes = False

@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'

@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

@app.route('/python/<text>')
def python_page(text='is cool'):
    '''The python page.'''
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
