""" Admin de Libros"""

# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from books.models.books import Books
from books.models.users_books import Users_Books


class CustomBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('title', 'author', 'year',)
    search_fields = ('title', 'author',)

class CustomUserBooksAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'id_book', 'read_date',)
    list_filter = ('id_profile', 'id_book', 'read_date',)


admin.site.register(Books, CustomBookAdmin)
admin.site.register(Users_Books, CustomUserBooksAdmin)