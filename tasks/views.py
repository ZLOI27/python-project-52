from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"


class TaskDetailView(LoginRequiredMixin, ListView):
    pass


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    pass


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    pass


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    pass
