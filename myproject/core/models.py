from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
        
class Negocio(models.Model):
    title = models.CharField(max_length=255)
    negocio_slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name="negocios", on_delete=models.CASCADE)
    description = models.TextField()
    cat_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField(max_length = 254)
    description = models.TextField()

    def __str__(self):
        return self.name
