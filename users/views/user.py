""" View de Usuarios """

from django.shortcuts import render
from django.http import HttpResponse

def userView(request):
    return HttpResponse("UserView")