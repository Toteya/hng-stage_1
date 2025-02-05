#!/usr/bin/env python3
"""
module app:
Flask - Numbers Classification API
"""
from api.v1 import app_bp
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_bp)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

if __name__ == '__main__':
    host = '0.0.0.0'
    port = '5000'
    app.run(host=host, port=port, threaded=True)
