from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class BaseTestCase(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]


class AuthenticatedTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.get(username="admin")
        self.assertTrue(
            self.client.login(
                username="admin",
                password="password123",
            )
        )


class TaskListViewTest(AuthenticatedTestCase):
    def test_tasks_list(self):
        response = self.client.get(reverse("tasks:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/index.html")


class TaskDetailViewTest(AuthenticatedTestCase):
    def test_task_detail_view(self):
        task = Task.objects.get(pk=1)
        response = self.client.get(
            reverse("tasks:detail", kwargs={"pk": task.pk}),
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task.html")


class TaskCreateViewTest(AuthenticatedTestCase):
    def test_task_create_view(self):
        response = self.client.post(
            reverse("tasks:create"),
            {"name": "test_task_create"},
        )

        self.assertRedirects(response, reverse("tasks:index"))
        self.assertTrue(Task.objects.filter(name="test_task_create").exists())


class TaskUpdateViewTest(AuthenticatedTestCase):
    def test_task_update_view(self):
        task = Task.objects.get(pk=1)
        response = self.client.post(
            reverse("tasks:update", kwargs={"pk": task.pk}),
            {"name": "test_task_update"},
        )

        self.assertRedirects(response, reverse("tasks:index"))
        task.refresh_from_db()
        self.assertEqual(task.name, "test_task_update")


class TaskDeleteViewTest(AuthenticatedTestCase):
    def test_task_delete_view(self):
        task = Task.objects.get(pk=1)
        response = self.client.post(
            reverse("tasks:delete", kwargs={"pk": task.pk}),
        )

        self.assertRedirects(response, reverse("tasks:index"))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_delete_task_not_author(self):
        task = Task.objects.get(pk=1)
        self.client.logout()

        self.assertTrue(
            self.client.login(
                username="petrov",
                password="password123",
            )
        )

        response = self.client.post(
            reverse("tasks:delete", args=[task.pk]),
        )

        self.assertRedirects(
            response,
            reverse("tasks:index"),
        )

        self.assertTrue(Task.objects.filter(pk=task.pk).exists())
