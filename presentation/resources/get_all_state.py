from __future__ import print_function
import sys
import numpy as np
from flask import current_app, Response

from flask_restful import Resource
from bson.json_util import dumps

from domain.interface_adapters.city_adapter import CityAdapter
from data.repositories.city import CityRepository
from presentation.schemas.city import CitySchema

class MasterStatesResource(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adapter = CityAdapter(
            repository=CityRepository(
                database_connection=current_app.mongo_connection
            )
        )

    def get(self):
        configuration = self.adapter.getAllState()
        output = []
        for conf in configuration:
            schema = CitySchema().dump(conf)
            output.append(schema['state'])
        response_data = np.unique(output).tolist()
        return ({'message': 'Success', 'data' : response_data})