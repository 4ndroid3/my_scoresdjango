""" View de Libros """

# from django.shortcuts import render
# from django.http import HttpResponse

# def bookView(request):
#     return HttpResponse("BookView")

from django.http import HttpResponse
from django.views import View

class BookView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('BookView')