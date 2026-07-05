from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


