from django.shortcuts import redirect, render

from .forms import AutorForm, BusquedaAutorForm, LibroForm 
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

# Vista para el formulario de búsqueda de libros por nombre y apellido del autor
    

def libros_por_autor(request):
    form = BusquedaAutorForm()
    libros = None
    autor = None

    if request.method == 'POST':
        form = BusquedaAutorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            try:
                autor = Autor.objects.get(nombre=nombre, apellido=apellido)
                # Usamos el campo 'autores' que descubrimos antes por el error
                libros = Libro.objects.filter(autores=autor)
            except Autor.DoesNotExist:
                libros = [] # Autor no encontrado

    return render(request, 'bibliotecaApp/busquedalibro.html', {
        'form': form,
        'libros': libros,
        'autor': autor
    })