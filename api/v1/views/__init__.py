#!/usr/bin/python3
'''
definitions and import for the flask app
'''

from flask import Blueprint
from models import storage, storage_type, db
from models.engine import valid_models

app_views = Blueprint('views', __name__, url_prefix='/api/v1')
storage = storage
valid_models = valid_models
storage_type = storage_type
db = db

# pep8 will dislike this, but `__init__.py` wont be
# checked but this will prevent circular imports later
from api.v1.views.index import *
# from api.v1.views.amenities import *
from api.v1.views.users import *
