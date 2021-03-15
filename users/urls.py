""" URLS de Users """

# Django Imports
from django.urls import path

# Project Imports
from users.views import user, profile
from .views.user_books import ReadedBookList, ReadedBookDetail, ReadedBookCreate, ReadedBookUpdate, ReadedBookDelete


urlpatterns = [
    path(
        route = 'user', 
        view = user.userView, 
        name = 'user'
    ),
    path(
        route = 'user/profile', 
        view = profile.profileView, 
        name = 'profile'
    ),
    path(
        route = 'user/readed/', 
        view = ReadedBookList.as_view(), 
        name = 'readed_list'
    ),
    path(
        route = 'user/readed/create/', 
        view = ReadedBookCreate.as_view(), 
        name = "readed_create"
    ),
    path(
        route = 'user/readed/update/<int:pk>', 
        view = ReadedBookUpdate.as_view(), 
        name = "readed_update"
    ),
    path(
        route = 'user/readed/delete/<int:pk>', 
        view = ReadedBookDelete.as_view(), 
        name = "readed_delete"
    ),
    path(
        route = 'user/readed/<int:pk>/', 
        view = ReadedBookDetail.as_view(), 
        name = "readed_detail"
    ),
]
