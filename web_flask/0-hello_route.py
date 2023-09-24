#!/usr/bin/python3

"""
Create a Flask web application.
"""

from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

if __name__ == "__main__":
    # Run the application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
