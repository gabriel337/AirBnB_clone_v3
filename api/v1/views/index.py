#!/usr/bin/python3
"""
routes:
    /status: display "status":"OK"
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    '''
        return JSON of OK status
    '''
    return jsonify({'status': 'OK'})


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

