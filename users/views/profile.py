""" View del Perfil de usuario """

# Django Imports
from django.shortcuts import render
from django.http import HttpResponse

# Project Imports
from users.models.profile import Profile
from users.models.users import User



def profileView(request):
    user = User.objects.get(username = request.user.username)
    print(type(user))
    dato_usuario = Profile.objects.get(id_users = user)
    context = {
        'dato_usuario' : dato_usuario,
    }
    return render(request, 'users/profile_detail.html', context)