#!/usr/bin/python3

'''
A basic web application built with Flask.
'''

from flask import Flask


app = Flask(__name__)

'''
The instance of the Flask application
'''

app.url_map.strict_slashes = False


@app.route('/')
def index():

    '''
    Home page.
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
