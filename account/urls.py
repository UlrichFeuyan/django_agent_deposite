from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'account'
urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('profil/', profil, name='profil'),
    path('dashboard/', redirect_user, name='redirect_user'),

    path('inscription/', Register.as_view(), name='register'),
    path('changepassword/', ChangePassword.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
