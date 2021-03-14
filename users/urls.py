""" URLS de Users """

# Django Imports
from django.urls import path

# Project Imports
from users.views import user, profile
from .views.user_books import ReadedBookList, ReadedBookDetail, ReadedBookCreate, ReadedBookUpdate, ReadedBookDelete


urlpatterns = [
    path('user', user.userView, name = 'user'),
    path('user/profile', profile.profileView, name = 'profile'),
    path('user/readed/', ReadedBookList.as_view(), name = 'readed_list'),
    path('user/readed/create/', ReadedBookCreate.as_view(), name = "readed_create"),
    path('user/readed/update/<int:pk>', ReadedBookUpdate.as_view(), name = "readed_update"),
    path('user/readed/delete/<int:pk>', ReadedBookDelete.as_view(), name = "readed_delete"),
    path('user/readed/<int:pk>/', ReadedBookDetail.as_view(), name = "readed_detail"),
    
]
