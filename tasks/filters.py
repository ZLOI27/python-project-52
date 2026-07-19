import django_filters
from django.contrib.auth.models import User

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

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
    )

    self_tasks = django_filters.BooleanFilter(
        method="filter_self_tasks",
        label="Только свои задачи",
    )

    class Meta:
        model = Task
        fields = [
            "status",
            "executor",
            "labels",
        ]

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
