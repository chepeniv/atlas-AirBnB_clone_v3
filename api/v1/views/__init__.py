from flask import Blueprint


app_views = Blueprint('views', __name__, url_prefix='/api/v1')
# documentation for positional arguments name and
# import_name not found in pydoc3

from api.v1.views.index import *
# pep8 will dislike this, but `__init__.py` wont be
# checked this will prevent circular imports later
