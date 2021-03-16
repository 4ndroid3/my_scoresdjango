""" URLS de Books """

# Django Imports
from django.urls import path

# Project Imports
from .views.book import (
    BookList,
    BookDetail,
    BookCreation,
    BookUpdate,
    BookDelete,
)
    

""" 
GET /books (listar todos los libros)
GET /books/<id> (traer un libro en especifico)
POST /books (crear libro)
DELETE /books/<id> (eliminar un libro)

GET /books/readed (listar todos los libros leidos por el usuario logueado)
GET /books/readed/<id> (traer un libro especifico leido por el usuario logueado)
POST /books/readed/ (crea un libro leido por el usuario logueado)
DELETE /books/readed/<id> (elimina un libro especifico leido por el usuario logueado)
"""

urlpatterns = [
    
    path(route = 'books/', view = BookList.as_view(), name = 'list'),
    path(route = 'books/<pk>/', view = BookDetail.as_view(), name = 'detail'),
    path(route = 'books/create', view = BookCreation.as_view(), name = 'create'),
    path(route = 'books/update/<pk>', view = BookUpdate.as_view(), name = 'update'),
    path(route = 'books/delete/<pk>', view = BookDelete.as_view(), name = 'delete'),
]
