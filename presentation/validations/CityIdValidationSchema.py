from marshmallow import Schema, fields, validate, EXCLUDE



class CityIdValidationSchema(Schema):
    cityId = fields.Str(required=True)

    class Meta:
        unknown = EXCLUDE
