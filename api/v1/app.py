#!/usr/bin/python3

"""
App
"""


from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0"}})

@app.errorhandler(404)
def not_found(error):
    """Error Handles"""
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response


@app.teardown_appcontext
def teardown(exception):
    """Teardown Function"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
