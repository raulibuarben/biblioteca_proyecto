from django.urls import include, path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),


]