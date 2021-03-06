""" View del Perfil de usuario """

from django.shortcuts import render
from django.http import HttpResponse

def profileView(request):
    return HttpResponse("ProfileView")