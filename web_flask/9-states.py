#!/usr/bin/python3
"""
Enumerates states
"""


from flask import Flask
from flask import render_template
from flask import session
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Enumerates states
    """
    storage.reload()
    cities = None
    states_dict = storage.all("State")
    states = []
    for s, k in states_dict.items():
        states.append([v.id, v.name])
    return render_template('9-states.html', states=states,
                           cities=cities, id=None)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    lists states
    """
    storage.reload()
    cities_dict = storage.all("City")
    states_dict = storage.all("State")
    cities_states = []
    states = []
    state = []
    for s, k in states_dict.items():
        states.append([v.id, v.name])
    for city in cities_dict.values():
        if city.state_id == id:
            cities_states.append([city.id, city.name])
    for i in states:
        if i[0] == id:
            state.append([s[0], s[1]])
    if (len(state) != 0):
        state = state[0][1]
    if (len(cities_states) != 0 and len(state) != 0):
        return render_template('9-states.html', states=state,
                               cities=cities_states, id=id)
    return render_template('9-states.html', states=None, cities=None, id=0)


@app.teardown_appcontext
def teardown_db(error):
    """
    Enumerates states
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
