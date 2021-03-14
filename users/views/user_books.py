""" View de Libros leidos por usuario"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Project Imports
from users.models.users_books import Users_Books

class ReadedBookList(LoginRequiredMixin, ListView):
    """ Lista todos los libros cargados"""

    model = Users_Books
    ordering = 'pk'

class ReadedBookDetail(LoginRequiredMixin, DetailView):
    """Detalle de un libro leido en especifico"""
    model = Users_Books
    
    
class ReadedBookCreate(LoginRequiredMixin, CreateView):
    """ agrega un nuevo libro leido"""

    model = Users_Books
    fields = ['id_profile', 'id_book', 'read_date', 'review']
    success_url = reverse_lazy('readed_list')

class ReadedBookUpdate(LoginRequiredMixin, UpdateView):
    """ Editar o actualizar un libro 
    Necesita:
    Modelo, 
    La URL a la que debe redireccionar cuando concluya la creación,
    Campos que usará para la creación, 
    """
    model = Users_Books
    fields = ['id_profile', 'id_book', 'read_date', 'review']
    success_url = reverse_lazy('readed_list')

class ReadedBookDelete(LoginRequiredMixin, DeleteView):
    """ 
    Eliminar un libro
    Necesita:
    Modelo,
    La URL a la que debe redireccionar cuando concluya la creación,
    """
    model = Users_Books
    success_url = reverse_lazy('readed_list')