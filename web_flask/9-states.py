#!/usr/bin/python3
"""
This script initiates a Flask-based web application
"""

from flask import Flask
from flask import render_template
from models.state import State
import subprocess
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    This function is triggered when a request is made to
    0.0.0.0:5000/states
    """
    state_list = storage.all(State)
    states = []
    for value in state_list.values():
        states.append(value)
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def single_state(id):
    """
    This function runs upon a request to 0.0.0.0:5000/states.
    """
    state_list = storage.all(State)
    state = {}
    for key, value in state_list.items():
        if value.id == id:
            state = state_list[key]
    return render_template('9-states.html', id=id, state=state)


@app.teardown_appcontext
def tear_down_context(exception):
    """
    This function deletes the existing SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=9-states.py")
    subprocess.run("flask run")
