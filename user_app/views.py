from django.shortcuts import render
from django.views.generic import CreateView
from user_app.models import MyCustomUser
from django.urls import reverse_lazy
from user_app.forms import MyCustomUserCreationForm

class Register(CreateView):
    form_class = MyCustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')