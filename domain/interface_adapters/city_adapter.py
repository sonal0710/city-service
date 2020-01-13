import os
from typing import Dict

from data.repositories.city import CityRepository
from domain.entities.city import City

""" Here goes the bridge between, reposityry, and use cases"""

class CityAdapter(object):

    def __init__(self, repository: CityRepository):
        self.repository = repository
    


    def get(self) -> City:
        configuration = self.repository.get_configuration()
        return self._configuration_to_entity(configuration=configuration)

    

    @classmethod
    def _configuration_to_entity(cls, configuration: Dict) -> City:
        output = []
        for conf in configuration:
            configuration_entity = City(
                id=conf.get("_id") or "",
                cityName=conf.get("city") or "",
                currency=conf.get("currency") or "",
                currencySymbol=conf.get("currencySymbol") or ""
            )
            output.append(configuration_entity)
        return output


