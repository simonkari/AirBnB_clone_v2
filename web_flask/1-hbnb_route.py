#!/usr/bin/python3
'''A simple Flask web application.'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
