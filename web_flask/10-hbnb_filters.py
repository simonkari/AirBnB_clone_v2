#!/usr/bin/python3
""" List of states """


from flask import Flask
from flask import session
from models import storage
from flask import render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """lists states"""
    storage.reload()
    cities_dict = storage.all("City")
    states_dict = storage.all("State")
    amenity_dict = storage.all("Amenity")
    states = []
    cities = {}
    amenities = []
    for k, v in states_dict.items():
        states.append([v.id, v.name])
    for city in cities_dict.values():
        if city.state_id in cities.keys():
            cities[city.state_id].append([city.id, city.name])
        else:
            cities[city.state_id] = [[city.id, city.name]]
    for k, v in amenity_dict.items():
        amenities.append(v.name)
    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(error):
    """lists states"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
