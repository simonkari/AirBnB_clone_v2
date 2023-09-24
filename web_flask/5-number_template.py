#!/usr/bin/python3

'''
A simple Flask web app.
'''

from flask import Flask, render_template

app = Flask(__name__)

# Disable strict slashes for URL routing
app.url_map.strict_slashes = False

@app.route('/')
def index():
    '''Main page.'''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''HBNB page.'''
    return 'HBNB'

@app.route('/c/<text>')
def c_page(text):
    '''C page.'''
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''Python page.'''
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number_page(n):
    '''Number page.'''
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    '''Number template page.'''
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
