from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


app_name = 'account'
urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('profil/', Profil.as_view(), name='profil'),

    path('changepassword/', ChangePassword.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
