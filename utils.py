from typing import Dict
from flask import make_response, jsonify

from configuration import MONGODB_URI, ENVIRONMENT

def is_production() -> bool:
    return ENVIRONMENT == "production"



