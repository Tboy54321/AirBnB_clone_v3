#!/usr/bin/python3
"""App"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
'''api = Api(app)'''
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
