from django.contrib import admin

from .models import Autor, Libro

# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)