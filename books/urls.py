""" URLS de Books """

# Django Imports
from django.urls import path

# Project Imports
from .views import user_books
from .views.book import BookView

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
    # path('book', book.bookView),
    path('books', BookView.as_view()),
    path('books/readed/', user_books.readedBookView)
]
