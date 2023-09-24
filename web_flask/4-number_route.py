#!/usr/bin/python3
""" 
Hello World in Flask
"""

# Import the Flask framework
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_world():
    """
    Route for the root URL
    """
    return 'Hello HBNB!'

# Define a route for the URL '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route for '/hbnb'
    """
    return 'HBNB'

# Define a route for URLs starting with '/c/' followed by a variable 'text'
@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """
    Route for '/c/<text>'
    Replaces underscores in 'text' with spaces
    """
    return 'C %s' % text.replace('_', ' ')

# Define a route for the URL '/python' with an optional variable 'text'
# Defaults to 'is cool' if 'text' is not provided
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ctextdefault(text):
    """
    Route for '/python' with an optional 'text' parameter
    Replaces underscores in 'text' with spaces
    """
    return 'Python %s' % text.replace('_', ' ')

# Define a route for URLs starting with '/number/' followed by an integer 'n'
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route for '/number/<int:n>'
    Responds with a message indicating that 'n' is a number
    """
    return '%d is a number' % n

# Run the Flask application if this script is the main program
if __name__ == '__main__':
    app.run(host='0.0.0.0')
