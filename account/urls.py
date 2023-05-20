from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'account'
urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('profil/', profil, name='profil'),

    path('users/', users, name='users'),
    path('users/user/', user_list, name='user_list'),
    path('users/user/add', add_user, name='add_user'),
    path('users/user/<str:pk>/remove', remove_user, name='remove_user'),
    path('users/user/<str:pk>/edit', edit_user, name='edit_user'),

    path('inscription/', Register.as_view(), name='register'),
    path('changepassword/', ChangePassword.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
