from ninja import NinjaAPI
from core.models import Category, Negocio, Contact
from typing import List
from core.schema import NegocioSchema, NotFoundSchema, CategorySchema, ContactSchema

api = NinjaAPI()


@api.post("/contact", response={201: ContactSchema})
def create_contact(request, contact: ContactSchema):
    contact = Contact.objects.create(**contact.dict())
    return contact

@api.get("/contact", response=List[ContactSchema])
def negocios(request):
    return Contact.objects.all()



@api.get("/categories", response=List[CategorySchema])
def negocios(request):
    return Category.objects.all()

##GET REQUEST
@api.get("/negocios", response=List[NegocioSchema])
def negocios(request):
    return Negocio.objects.all()

##GET BY ID REQUEST 
@api.get("/negocios/{negocio_id}", response={200: NegocioSchema, 404:NotFoundSchema})
def negocio(request, negocio_id: int):
    try:
        negocio = Negocio.objects.get(pk=negocio_id)
        return 200, negocio
    except Negocio.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}

#POST REQUEST
@api.post("/negocios", response={201: NegocioSchema})
def create_negocio(request, negocio: NegocioSchema):
    negocio = Negocio.objects.create(**negocio.dict())
    return negocio

#DELETE REQUEST
@api.put("/negocios/{negocio_id}", response={200: NegocioSchema, 404:NotFoundSchema})
def change_negocio(request, negocio_id: int, data: NegocioSchema):
    try:
        negocio = Negocio.objects.get(pk=negocio_id)
        for attribute, value in data.dict().items():
             setattr(negocio, attribute, value)
        negocio.save()
        return 200, negocio
    except Negocio.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}

#DELETE REQUEST
@api.delete("/negocios/{negocio_id}", response={200:None, 404:NotFoundSchema})
def delete_negocio(request, negocio_id: int, data: NegocioSchema):
    try:
        negocio = Negocio.objects.get(pk=negocio_id)
        negocio.delete()
        return 200 
    except Negocio.DoesNotExist as e:
        return 404, {"message": "Negocio no existe"}

