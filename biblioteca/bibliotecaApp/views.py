from django.shortcuts import render
from .models import Libro

# Create your views here.
#Vista para mostrar la lista de libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'bibliotecaApp/lista_libros.html', {'libros': libros})




