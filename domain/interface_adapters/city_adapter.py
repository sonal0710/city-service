from __future__ import print_function
import sys
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
                city=conf.get("city") or "",
                currency=conf.get("currency") or "",
                currencySymbol=conf.get("currencySymbol") or "",
                country=conf.get("country") or ""
            )
            output.append(configuration_entity)
        return output

    def getById(self, cityId) -> City:
        configuration = self.repository.get_city_by_id(cityId)
        return self._configuration_to_entity_city_by_id(configuration=configuration)

    @classmethod
    def _configuration_to_entity_city_by_id(cls, configuration: Dict) -> City:
        configuration_entity = City(
            id=configuration.get("_id") or "",
            city=configuration.get("city") or "",
            currency=configuration.get("currency") or "",
            currencySymbol=configuration.get("currencySymbol") or "",
            country=configuration.get("country") or "",
            state=configuration.get("state") or "",
            currencyAbbr=configuration.get("currencyAbbr") or "",
            currencyAbbrText=configuration.get("currencyAbbrText") or "",
            distanceMetrics=configuration.get("distanceMetrics") or "",
            distanceMetricsUnit=configuration.get("distanceMetricsUnit") or "",
            radiusforsomeOneElseBooking=configuration.get("radiusforsomeOneElseBooking") or "",
            maxEtaDistanceInMeters=configuration.get("maxEtaDistanceInMeters") or "",
            maxEtaTimeInSeconds=configuration.get("maxEtaTimeInSeconds") or "",
            isTipEnable=configuration.get("isTipEnable") or "",
            tipType=configuration.get("curretipTypency") or "",
            paymentMode=configuration.get("paymentMode") or "",
            paymentGateways=configuration.get("paymentGateways") or "",
            isCorporateEnable=configuration.get("isCorporateEnable") or "",
            isFavoriteDriverEnable=configuration.get("isFavoriteDriverEnable") or "",
            isDeleted=configuration.get("isDeleted") or "",
            location=configuration.get("location") or "",
            timeOffset=configuration.get("timeOffset") or "",
            polygons=configuration.get("polygons") or "",
            pointsProps=configuration.get("pointsProps") or "",
            dstOffset=configuration.get("dstOffset") or "",
            timeZoneId=configuration.get("timeZoneId") or "",
            walletSettings=configuration.get("walletSettings") or "",
            isPreferenceEnabled=configuration.get("isPreferenceEnabled") or "",
            cityStatus=configuration.get("cityStatus") or ""
        )
        return configuration_entity

    def getAllState(self) -> City:
        configuration = self.repository.get_all_state()
        return self._configuration_to_entity_get_state(configuration=configuration)

    @classmethod
    def _configuration_to_entity_get_state(cls, configuration: Dict) -> City:
        output = []
        for conf in configuration:
            configuration_entity = City(
                state=conf.get("state") or ""
            )
            output.append(configuration_entity)
        return output

    def getCitiesByState(self, state) -> City:
        configuration = self.repository.get_cities_from_state(state)
        return self._configuration_to_entity_get_cities(configuration=configuration)

    @classmethod
    def _configuration_to_entity_get_cities(cls, configuration: Dict) -> City:
        output = []
        for conf in configuration:
            configuration_entity = City(
                id=conf.get("_id") or "",
                city=conf.get("city") or ""
            )
            output.append(configuration_entity)
        return output