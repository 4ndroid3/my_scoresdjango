""" View de Usuarios """
# Django Imports
from django.shortcuts import render
from django.http import HttpResponse

# Project Imports
from users.models.users import User

def userView(request):
    dato_usuario = User.objects.get(username= request.user.username)
    context = {
        'dato_usuario' : dato_usuario,
    }
    return render(request, 'users/user_detail.html', context)