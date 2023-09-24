#!/usr/bin/python3
""" List of states """


from flask import Flask
from flask import session
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_ofstate():
    """cities of a state"""
    storage.reload()
    cities_dict = storage.all("City")
    states_dict = storage.all("State")
    cities_states = {}
    states = []
    for k, v in states_dict.items():
        states.append([v.id, v.name])
    for city in cities_dict.values():
        if city.state_id in cities_states.keys():
            cities_states[city.state_id].append([city.id, city.name])
        else:
            cities_states[city.state_id] = [[city.id, city.name]]
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities_states)


@app.teardown_appcontext
def teardown_db(error):
    """lists states"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
