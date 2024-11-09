# `from flask import Blueprint`
# create variable `app_views` instance of `Blueprint` (url prefix `/api/v1`)
# "below the above line for app_views" add a wildcard import of everything in
#       the package `api.v1.views.index`
# pep8 will dislike this, but `__init__.py` wont be checked this will prevent
#       circular imports later
