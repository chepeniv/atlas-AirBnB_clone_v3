#!/usr/bin/python3
'''
definitions and import for the flask app
'''

from flask import Blueprint

app_views = Blueprint('views', __name__, url_prefix='/api/v1')

# pep8 will dislike this, but `__init__.py` wont be
# checked but this will prevent circular imports later
from api.v1.views.index import *
from api.v1.views.amenities import *
from api.v1.views.users import *
