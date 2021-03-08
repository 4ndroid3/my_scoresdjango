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

class BookDetail(DetailView):
    """ Detalle de un curso en especifico"""
    model = Books

class BookCreation(CreateView):
    """ Creacion de un nuevo libro 
    Necesita:
    Modelo, 
    La URL a la que debe redireccionar cuando concluya la creación,
    Campos que usará para la creación, 
    """
    model = Books.objects.all()
    fields = ['title', 'author']
    success_url = reverse_lazy('books:list')

class BookUpdate(UpdateView):
    """ Editar o actualizar un libro 
    Necesita:
    Modelo, 
    La URL a la que debe redireccionar cuando concluya la creación,
    Campos que usará para la creación, 
    """
    model = Books.objects.all()
    fields = ['title', 'author']
    success_url = reverse_lazy('books:list')

class BookDelete(DeleteView):
    """ 
    Eliminar un libro
    Necesita:
    Modelo,
    La URL a la que debe redireccionar cuando concluya la creación,
    """
    model = Books.objects.all()
    success_url = reverse_lazy('books:list')