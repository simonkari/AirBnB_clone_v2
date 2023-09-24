#!/usr/bin/python3
""" List of states """


from flask import Flask
from flask import session
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """lists states"""
    storage.reload()
    states_dict = storage.all("State")
    states = []
    for k, v in states_dict.items():
        states.append([v.id, v.name])
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(error):
    """lists states"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
