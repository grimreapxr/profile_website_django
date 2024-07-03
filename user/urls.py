from django.urls import path
from .views import *

urlpatterns = [
    path('',homePage, name ='home'),
    path('login/',loginPage, name = 'login'),
    path('logout/',logoutUser, name = 'logout'),
    path('signup/',register, name ='register'),
    path('profile/',profilePage, name ='profile'),
    path('change_password/',ChangePasswordPage.as_view(), name ='cpass')
]