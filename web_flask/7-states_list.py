#!/usr/bin/python3

'''
An uncomplicated Flask web application.
'''

from flask import Flask, render_template

from models.state import State
from models import storage


app = Flask(__name__)
'''
The instance of the Flask application
'''
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''
    The page titled states_list
    '''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''
    The event listener for the Flask app/request context ending.
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
