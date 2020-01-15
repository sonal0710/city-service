from __future__ import print_function
import sys
from flask import current_app, Response

from flask_restful import Resource
from bson.json_util import dumps

from domain.interface_adapters.city_adapter import CityAdapter
from data.repositories.city import CityRepository
from presentation.schemas.city import CitySchema

class MasterCitiesByStateResource(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adapter = CityAdapter(
            repository=CityRepository(
                database_connection=current_app.mongo_connection
            )
        )

    def get(self, state:str):
        configuration = self.adapter.getCitiesByState(state)
        output = []
        for conf in configuration:
            schema = CitySchema().dump(conf)
            output.append(schema)
        return ({'message': 'Success', 'data' : output})