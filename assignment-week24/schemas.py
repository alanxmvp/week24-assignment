from marshmallow_sqlalchemy import ModelSchema
from models import Homes


class HomeSchema(ModelSchema):
    class Meta:
        model = Homes