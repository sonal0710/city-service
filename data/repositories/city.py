from __future__ import print_function
import sys
from flask import current_app
from bson import ObjectId

class CityRepository(object):

    def __init__(self, database_connection, collection_name='cities'):
        self.collection_name = collection_name
        self.database_connection = database_connection
    

    def get_database(self):
        return self.database_connection[self.collection_name]
    

    def get_configuration(self):
        return self.get_database().find({ "isDeleted": { "$ne": True } })

    def get_city_by_id(self, cityId):
        return self.get_database().find_one({ '_id': ObjectId(cityId['cityId']) })
         
    def get_all_state(self):
        return self.get_database().find({ "isDeleted": { "$ne": True }, "cityStatus": "1" })

    def get_cities_from_state(self, state):
        return self.get_database().find({ "state": state, "isDeleted": False, 'cityStatus' : '1'  })