from typing import Dict, Tuple
from functools import wraps
from marshmallow import exceptions


def build_validation_error_response(*, errors: Dict) -> Tuple:
    return {'errors': errors}, 422


def parse_validation_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exceptions.ValidationError as e:
            return build_validation_error_response(errors=e.messages)
    return wrapper
            

