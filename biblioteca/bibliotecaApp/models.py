import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
#Modelo para los libros de la biblioteca, pueden tener varios autores
class Libro(models.Model):  
    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField('Autor')
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.titulo
    
#Modelo para los autores de los libros
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"