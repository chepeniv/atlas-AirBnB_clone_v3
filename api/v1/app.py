# create variable `app` instance of `Flask`
# `from models import storage`
# `from api.v1.views import app_views`
# register the blueprint `app_views` to the `Flask` instance `app`
# declare a method to handle `@app.teardown_appcontext`
    # call `storage.close()`
# within `if __name__ == "__main__":`
    # run the Flask server `app`
        # set `host=HBNB_API_HOST` or `0.0.0.0` if not defined
        # set `port=HBNB_API_PORT` or `5000` if not defined
        # set `threaded=True`
