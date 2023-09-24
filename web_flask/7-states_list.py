#!/usr/bin/python3

'''
An uncomplicated Flask web application.
'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
# Enable debugging during development
app.config['DEBUG'] = True
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''
    The page named states_list
    '''
    try:
        all_states = list(storage.all(State).values())
        all_states.sort(key=lambda x: x.name)
        ctxt = {
            'states': all_states
        }
        return render_template('7-states_list.html', **ctxt)
    except Exception as e:
        # Handle exceptions, log the error, and provide a user-friendly error message
        app.logger.error(f"An error occurred: {e}")
        return "An error occurred while processing your request."


@app.teardown_appcontext
def flask_teardown(exc):
    '''
    The Flask app/request context end event listener.
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
