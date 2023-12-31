#!/usr/bin/python3

'''
An uncomplicated Flask web application.
'''

from flask import Flask, render_template


app = Flask(__name__)
'''
The instance of the Flask application.
'''

app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''
    Main page.
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


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''
    python page.
    '''

    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''
    The page related to numbers.
    '''

    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    The page titled 'number_template'.
    '''

    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
