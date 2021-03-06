""" View de Libros """

from django.shortcuts import render
from django.http import HttpResponse

def bookView(request):
    return HttpResponse("BookView")