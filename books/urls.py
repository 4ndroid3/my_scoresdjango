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
from .views.user_books import ReadedBookList
    

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
    #path('', BookList.as_view(), name = 'list'),
    
    path('books', BookList.as_view(), name = 'list'),
    path('books/<pk>', BookDetail.as_view(), name = 'detail'),
    path('books/create',BookCreation.as_view(), name = 'create'),
    path('books/update/<pk>',BookUpdate.as_view(), name = 'update'),
    path('books/delete/<pk>', BookDelete.as_view(), name = 'delete'),
    path('readed', ReadedBookList.as_view(), name = 'readed')
]
