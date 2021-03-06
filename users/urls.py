""" URLS de Users """

# Django Imports
from django.urls import path

# Project Imports
from .views import profile, user

urlpatterns = [
    path('user', user.userView),
    path('user/profile/', profile.profileView)
]
