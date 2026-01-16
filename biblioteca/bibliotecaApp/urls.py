from django.urls import include, path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('insertarlibro/', views.insertar_libro, name='insertar_libro'),
    path('insertarautor/', views.insertar_autor, name='insertar_autor'),


]