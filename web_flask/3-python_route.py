#!/usr/bin/python3

'''
A basic Flask web application.
'''

# Import the Flask framework and render_template function
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Disable strict slashes for URL routing
app.url_map.strict_slashes = False

# Define a route for the root URL '/'
@app.route('/')
def index():
    '''
    Main page.
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
@app.route('/python')
def python_page(text='is cool'):
    '''
    python page.
    '''
    return 'Python {}'.format(text.replace('_', ' '))

# Define a route for URLs starting with '/number/' followed by an integer 'n'
@app.route('/number/<int:n>')
def number_page(n):
    '''
    Number page.
    '''
    return '{} is a number'.format(n)

# Define a route for URLs starting with '/number_template/' followed by an integer 'n'
@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    The page named number_template
    '''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)

# Define a route for URLs starting with '/number_odd_or_even/' followed by an integer 'n'
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''
    The page titled 'number_odd_or_even
    '''
    ctxt = {
        'n': n
    }
    return render_template('6-number_odd_or_even.html', **ctxt)

# Run the Flask application if this script is the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
