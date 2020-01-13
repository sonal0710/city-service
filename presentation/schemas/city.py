from marshmallow import Schema, fields

class CitySchema(Schema):

    id = fields.Str(data_key="id")
    cityName = fields.Str(data_key="cityName")
    currency = fields.Str(data_key="currency")
    currencySymbol = fields.Str(data_key="currencySymbol")