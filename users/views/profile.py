""" View del Perfil de usuario """

# Django Imports
from django.shortcuts import render
from django.http import HttpResponse

# Project Imports
from users.models.profile import Profile

def profileView(request):
    return HttpResponse("ProfileView")