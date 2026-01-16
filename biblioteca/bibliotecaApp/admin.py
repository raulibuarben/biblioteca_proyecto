from django.contrib import admin

from biblioteca.bibliotecaApp.models import Autor, Libro

# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)