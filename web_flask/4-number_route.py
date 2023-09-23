#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debugging during development
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
    return f'C {text.replace("_", " ")}'

@app.route('/python/<text>')
@app.route('/python')
def python_page(text='is_cool'):
    '''The python page.'''
    return f'Python {text.replace("_", " ")}'

@app.route('/number/<int:n>')
def number_page(n):
    '''The number page.'''
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
