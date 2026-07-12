"""from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class BaseTestCase(TestCase):
    fixtures = [
        "users.json",
        "statuses.json",
        "tasks.json"
    ]

class AuthenticatedTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.get(username="admin")
        self.assertTrue(
            self.client.login(
                username="admin",
                password="password123"
                )
        )

class TaskListViewTest(AuthenticatedTestCase):
    def test_task_page(self):
        response = self.client.get(reverse("tasks:index"))"""
