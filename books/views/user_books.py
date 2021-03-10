""" View de Libros leidos por usuario"""

# Django Imports
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Project Imports
from books.models.users_books import Users_Books

class ReadedBookList(ListView):
    """ Lista todos los libros cargados"""
    model = Users_Books

    ordering = 'pk'