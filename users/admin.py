# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from .models.users import User
from .models.profile import Profile
from .models.users_books import Users_Books

class CustomUserAdmin(UserAdmin):
    """Configuración del admin modificado"""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', )

class CustomProfileAdmin(admin.ModelAdmin):
    """ Configuracion de Muestra de Profiles en Admin"""
    list_display = ('id_users','country', 'birth_date', 'books_read', 'authors_read',)
    search_fields = ('id_users__email','id_users__username', 'id_users__first_name','id_users__last_name')

class CustomUserBooksAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'id_book', 'read_date',)
    list_filter = ('id_profile', 'id_book', 'read_date',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, CustomProfileAdmin)
admin.site.register(Users_Books, CustomUserBooksAdmin)