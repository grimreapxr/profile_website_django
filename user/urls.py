from django.urls import path
from .views import *

urlpatterns = [
    path('',homePage, name =' home'),
    path('login/',loginpage, name = 'login'),
    path('logout/',logoutUser, name = 'logout'),
    path('register/',registerpage, name ='register'),
]