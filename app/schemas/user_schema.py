from marshmallow import Schema, fields

class UserSchema(Schema):
    salary = fields.Float(required=True)
    sec80c = fields.Float()
    sec80d = fields.Float()
    home_loan = fields.Float()
