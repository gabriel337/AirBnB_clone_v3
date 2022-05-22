#!/usr/bin/python3
"""
routes:
    /status: display "status":"OK"
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route("/status")
def status():
    """return JSON of OK status"""
    dic = {'status': 'OK'}
    return jsonify(dic)


@app_views.route('stats')
def new_count():
    """endpoint that retrieves the number of each objects by type"""
    dic = {

            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return jsonify(dic)
