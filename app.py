from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_marshmallow import Marshmallow

from configuration import MONGODB_URI
from utils import is_production

from presentation.resources.city import CityResource
from presentation.resources.city_by_id import CityByIdResource
from presentation.resources.get_all_state import MasterStatesResource
from presentation.resources.get_cities_by_state import MasterCitiesByStateResource
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration



def set_sentry():
    sentry_sdk.init(
        dsn="https://e144abd7f4894bce9ca6466eaa0a27a1@sentry.io/1873245",
        integrations=[FlaskIntegration()]
    )

def set_resources(api):
    api.add_resource(CityResource, '/admin/city')
    api.add_resource(CityByIdResource, '/admin/cityDetailsByCityIds/<cityId>')
    api.add_resource(MasterStatesResource, '/master/state')
    api.add_resource(MasterCitiesByStateResource, '/master/city/<state>')


def set_marshmallow(app):
    ma = Marshmallow(app)
    return ma

def set_api(app):
    api = Api(app, catch_all_404s=True)
    set_resources(api)
    return api

def set_database(app):
    app.config["MONGO_URI"] = MONGODB_URI
    mongo = PyMongo(app)
    app.mongo_connection = mongo.db
    return mongo

def create_app():
    app = Flask("city-service")
    set_database(app)
    set_api(app)
    set_marshmallow(app)
    app.run(debug=not is_production, host="0.0.0.0")

if __name__ == "__main__":
    create_app()