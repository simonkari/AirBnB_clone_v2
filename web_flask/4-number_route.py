#!/usr/bin/python3

'''
An uncomplicated Flask web application.
'''

# Import the Flask framework
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Disable strict slashes for URL routing
app.url_map.strict_slashes = False

# Define a route for the root URL '/'
@app.route('/')
def index():
    '''
    The main page.
    '''
    return 'Hello HBNB!'

# Define a route for the URL '/hbnb'
@app.route('/hbnb')
def hbnb():
    '''
    hbnb page.
    '''
    return 'HBNB'

# Define a route for URLs starting with '/c/' followed by a variable 'text'
@app.route('/c/<text>')
def c_page(text):
    '''
    c page.
    '''
    return 'C {}'.format(text.replace('_', ' '))

# Define a route for the URL '/python' with an optional variable 'text'
# Defaults to 'is cool' if 'text' is not provided
@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''
    python page.
    '''
    return 'Python {}'.format(text.replace('_', ' '))

# Define a route for URLs starting with '/number/' followed by an integer 'n'
@app.route('/number/<int:n>')
def number_page(n):
    '''
    The page related to numbers
    '''
    return '{} is a number'.format(n)

# Run the Flask application if this script is the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
