from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from labels.forms import LabelsForm
from labels.models import Label


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = "labels"


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelsForm
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels:index")
    success_message = _("Label created successfully")


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelsForm
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels:index")
    success_message = _("Label updated successfully")
    context_object_name = "label"


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels:index")
    success_message = _("Label deleted successfully")
    context_object_name = "label"
