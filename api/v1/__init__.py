#!/usr/bin/env python3
"""
Blueprint for API
"""
from flask import Blueprint

app_bp = Blueprint('app_bp', __name__, url_prefix='/api/v1')

from api.v1.numbers import *
