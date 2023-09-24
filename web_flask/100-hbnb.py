#!/usr/bin/python3
"""
Create a web app to display states, amenities, and places
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Get all states, amenities, and places from the database
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template(
        "100-hbnb.html", states=states, amenities=amenities, places=places
    )

@app.teardown_appcontext
def teardown(exc):
    """
    Close the SQLAlchemy session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
