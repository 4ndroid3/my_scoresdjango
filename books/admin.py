""" Admin de Libros"""

# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from books.models.books import Books


class CustomBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    list_filter = ('title', 'author', 'year',)
    search_fields = ('title', 'author',)
    
admin.site.register(Books, CustomBookAdmin)