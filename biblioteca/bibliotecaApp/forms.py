#Formulario para la inserción de libros
from django import forms
from .models import Libro, Autor

#Formulario para la inserción de libros
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'fecha_publicacion', 'isbn']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

#Formulario para la inserción de autores
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }   


# Formulario para la búsqueda de libros por nombre y apellido del autor
class BusquedaAutorForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Autor', max_length=100)
    apellido = forms.CharField(label='Apellido del Autor', max_length=100)    

    