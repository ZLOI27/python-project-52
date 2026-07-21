from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from users.forms import UserRegistrationForm, UserUpdateForm


class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    success_message = _("User registered successfully")


    def form_invalid(self, form):
        print(form.errors.as_json(), flush=True)
        return super().form_invalid(form)


class UserLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, _("You are logged in"))
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().post(request, *args, **kwargs)


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users:index")
    success_message = _("User updated successfully")

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != self.get_object().pk:
            messages.error(
                request, _("You have no permission to change another user")
            )
            return redirect("users:index")
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        messages.success(self.request, _("User deleted successfully"))
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != self.get_object().pk:
            messages.error(
                request, _("You have no permission to delete another user")
            )
            return redirect("users:index")

        return super().dispatch(request, *args, **kwargs)
