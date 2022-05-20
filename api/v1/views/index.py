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
