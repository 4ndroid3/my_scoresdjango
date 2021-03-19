""" View de Usuarios """
# Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Project Imports
from users.models.users import User

# def userView(request):
#     dato_usuario = User.objects.get(username= request.user.username)
#     context = {
#         'dato_usuario' : dato_usuario,
#     }
#     return render(request, 'users/user_detail.html', context)
class UserDetailView(LoginRequiredMixin, DetailView):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'dato_usuario'

class LoginUserView(LoginView):
    model = User
    success_url = reverse_lazy('profile')

class LogoutUserView(LoginRequiredMixin, LogoutView):
    model = User