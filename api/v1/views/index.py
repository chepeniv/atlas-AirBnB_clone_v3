#!/usr/bin/python3
'''
definitions of routes for the app_views blueprint
'''

from api.v1.views import app_views


@app_views.route('/status')
def status():
    '''
    return a json string denoting the status of the blueprint
    '''
    message = {"status": "OK"}
    # python objects are automatically returned as json by flask
    return message
