from api.v1.views import app_views
from json import dumps


@app_views.route('/status')
def status():
    message = {"status": "OK"}
    message = dumps(message)
    return message
