#!/usr/bin/python3
"""
starts flask app
"""
from flask import Flask, abort, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
app = Flask(__name__)


app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    '''
    close query after each session
    '''
    storage.close()


@app.errorhandler(404)
def resource_notfound(e):
    """404 on routes not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
