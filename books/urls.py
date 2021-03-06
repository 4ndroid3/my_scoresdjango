""" URLS de Books """

# Django Imports
from django.urls import path

# Project Imports
from .views import book, user_books

urlpatterns = [
    path('book', book.bookView),
    path('book/readed/', user_books.readedBookView)
]
