#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask

app = Flask(__name__)

# Disable strict slashes
app.url_map.strict_slashes = False

# Define routes and views
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
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''The python page.'''
    return 'Python {}'.format(text.replace('_', ' '))

# Run the application if executed as a script
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
