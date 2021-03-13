""" URLS de Users """

# Django Imports
from django.urls import path

# Project Imports
from .views import profile, user
from .views.user_books import ReadedBookList

urlpatterns = [
    path('user', user.userView),
    path('user/profile/', profile.profileView),
    path('user/readed', ReadedBookList.as_view())
]
