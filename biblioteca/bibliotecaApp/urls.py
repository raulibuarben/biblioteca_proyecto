from django.urls import include, path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('insertarlibro/', views.insertar_libro, name='insertar_libro'),
    path('insertarautor/', views.insertar_autor, name='insertar_autor'),


]