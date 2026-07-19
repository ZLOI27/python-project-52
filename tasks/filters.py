import django_filters
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from labels.models import Label
from statuses.models import Status
from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
    )

    label = django_filters.ModelChoiceFilter(
        field_name="labels",
        queryset=Label.objects.all(),
        label=_("Label"),
    )

    self_tasks = django_filters.BooleanFilter(
        method="filter_self_tasks",
        label=_("Only own tasks"),
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = Task
        fields = (
            "status",
            "executor",
            "label",
        )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
