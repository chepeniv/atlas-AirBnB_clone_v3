#!/usr/bin/python3
'''
definitions of routes for the app_views blueprint
'''

from api.v1.views import app_views, storage, valid_models


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
def count_each_model():
    '''
    retrieve and return the number of each object by type
    '''

    counts = {}
    for name, model in valid_models().items():
        count = storage.count(model)
        counts.update({name: count})

    return counts
