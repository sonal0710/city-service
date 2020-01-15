from flask import current_app, Response

from flask_restful import Resource
from bson.json_util import dumps

from domain.interface_adapters.city_adapter import CityAdapter
from data.repositories.city import CityRepository
from presentation.schemas.city import CitySchema
from presentation.validations.CityIdValidationSchema import CityIdValidationSchema
from validation_errors_utils import parse_validation_errors

class CityByIdResource(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adapter = CityAdapter(
            repository=CityRepository(
                database_connection=current_app.mongo_connection
            )
        )

    @parse_validation_errors
    def get(self, cityId):
        cityId = CityIdValidationSchema().load({ 'cityId':cityId })
        configuration = self.adapter.getById(cityId)
        schema = CitySchema().dump(configuration)
        return ({'message': 'Got The Details.', 'data' : schema})