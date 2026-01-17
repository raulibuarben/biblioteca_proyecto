from django.shortcuts import redirect, render

from .forms import AutorForm, LibroForm 
from .models import Autor, Libro

# Create your views here.
#Vista para mostrar la lista de libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'bibliotecaApp/lista_libros.html', {'libros': libros})

#Vista para mostrar la lista de autores
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'bibliotecaApp/lista_autores.html', {'autores': autores})


#Vista para formulario de inserción de libros
def insertar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'bibliotecaApp/insertar_libro.html', {'form': form})



# Vista para formulario de inserción de autores
def insertar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'bibliotecaApp/insertar_autor.html', {'form': form})


# Vista para la página de inicio
def inicio(request):
    return render(request, 'bibliotecaApp/inicio.html')

