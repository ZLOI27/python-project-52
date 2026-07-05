from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from users.forms import UserRegistrationForm


class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    success_message = _("User registered successfully")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.success(self.request, _("You are logged in"))
        return super().form_valid(form)


class UserUpdateView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
