#!/usr/bin/python3
"""List of states"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states():
    """Lists states"""
    storage.reload()
    states_dict = storage.all("State")
    states = [[v.id, v.name] for k, v in states_dict.items()]
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(error):
    """Closes the database connection"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
