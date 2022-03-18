from ninja import Schema, ModelSchema
from .models import Negocio, Category, Contact

class NegocioSchema(ModelSchema):
    class Config:
        model = Negocio
        model_fields = '__all__'
class NotFoundSchema(Schema):
    message: str

class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = '__all__'
class NotFoundSchema(Schema):
    message: str

class ContactSchema(ModelSchema):
    class Config:
        model = Contact
        model_fields = '__all__'
class NotFoundSchema(Schema):
    message: str
