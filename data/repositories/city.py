
from __future__ import print_function
import sys
from flask import current_app


class CityRepository(object):

    def __init__(self, database_connection, collection_name='cities'):
        self.collection_name = collection_name
        self.database_connection = database_connection
    

    def get_database(self):
        return self.database_connection[self.collection_name]
    

    def get_configuration(self):
        return self.get_database().find()