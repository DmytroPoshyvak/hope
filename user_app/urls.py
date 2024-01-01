from django.urls import path , include
from user_app import views
import django.contrib.auth

urlpatterns = [
    path('/' , include('django.contrib.auth.urls')),
    path('/register' , views.Register.as_view() , name = 'register'),
]