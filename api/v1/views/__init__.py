#!/usr/bin/python3
"""
init file
"""

from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.index import *
<<<<<<< HEAD
import api.v1.views.states
import api.v1.views.cities
import api.v1.views.amenities
#import api.v1.views.users
#import api.v1.views.places
#import api.v1.views.places_reviews
#import api.v1.views.places_amenities
=======
from api.v1.views.states import *
from api.v1.views.cities import *
>>>>>>> 8313ccc7fdc02ca0cbf2633bbca720134f85d7a7
