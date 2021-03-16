""" View de Usuarios """
# Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Project Imports
from users.models.users import User

def userView(request):
    dato_usuario = User.objects.get(username= request.user.username)
    context = {
        'dato_usuario' : dato_usuario,
    }
    return render(request, 'users/user_detail.html', context)

class LoginUserView(LoginView):
    model = User
    success_url = reverse_lazy('profile')

class LogoutUserView(LogoutView):
    model = User