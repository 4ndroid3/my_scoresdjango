""" View de Libros """

# Django Imports
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Project Imports
from books.models.books import Books


class BookList(ListView):
    """ Lista todos los libros cargados"""
    model = Books
    ordering = 'pk'
    

class BookDetail(DetailView):
    """ Detalle de un libro en especifico"""
    model = Books

class BookCreation(CreateView):
    """ Creacion de un nuevo libro 
    Necesita:
    Modelo, 
    La URL a la que debe redireccionar cuando concluya la creación,
    Campos que usará para la creación, 
    """
    model = Books
    fields = ['title', 'author', 'year', 'pages', 'img_cover']
    success_url = reverse_lazy('list')

class BookUpdate(UpdateView):
    """ Editar o actualizar un libro 
    Necesita:
    Modelo, 
    La URL a la que debe redireccionar cuando concluya la creación,
    Campos que usará para la creación, 
    """
    model = Books
    fields = ['title', 'author', 'year', 'pages', 'img_cover']
    success_url = reverse_lazy('list')

class BookDelete(DeleteView):
    """ 
    Eliminar un libro
    Necesita:
    Modelo,
    La URL a la que debe redireccionar cuando concluya la creación,
    """
    model = Books
    success_url = reverse_lazy('list')