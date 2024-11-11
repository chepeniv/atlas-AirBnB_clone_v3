#!/usr/bin/python3
'''
definitions of routes for the app_views blueprint
'''

from api.v1.views import app_views, storage


@app_views.route('/status')
def status():
    '''
    return a json string denoting the status of the blueprint
    '''
    message = {"status": "OK"}
    # python objects are automatically returned as json by flask
    return message

# route /api/v1/stats
@app_views.route('/stats')
def count_each():
    '''
    retrieve and return the number of each object by type
    '''

    # use storage.count()
    # json output example :
    # {
    # "amenities": 47,
    # "cities": 36,
    # "places": 154,
    # "reviews": 718,
    # "states": 27,
    # "users": 31
    # }

    return "count"
