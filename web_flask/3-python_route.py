#!/usr/bin/python3

'''
A straightforward Flask web application.
'''

from flask import Flask


app = Flask(__name__)
'''
The instance of the Flask application.
'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''
    The main page.
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    hbnb page.
    '''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''
    c page.
    '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_page(text):
    '''The python page.'''
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
