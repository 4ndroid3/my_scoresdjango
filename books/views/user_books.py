""" View de Libros leidos por usuario"""

from django.shortcuts import render
from django.http import HttpResponse

def readedBookView(request):
    return HttpResponse("ReadedBookView")