from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from statuses.models import Status


class AuthenticatedTestCase(TestCase):
    fixtures = [
        "users.json",
        "statuses.json",
    ]

    def setUp(self):
        super().setUp()
        self.user = User.objects.get(username="admin")
        self.assertTrue(
            self.client.login(
                username="admin",
                password="password123",
            )
        )


class StatusListViewTest(AuthenticatedTestCase):
    def test_status_page(self):
        response = self.client.get(reverse("statuses:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/index.html")


class StatusCreateViewTest(AuthenticatedTestCase):
    def test_create_status(self):
        response = self.client.post(
            reverse("statuses:create"),
            {"name": "test_status"},
        )

        self.assertRedirects(response, reverse("statuses:index"))
        self.assertTrue(Status.objects.filter(name="test_status").exists())


class StatusUpdateViewTest(AuthenticatedTestCase):
    def test_update_status(self):
        status = Status.objects.get(pk=1)
        response = self.client.post(
            reverse("statuses:update", kwargs={"pk": status.pk}),
            {"name": "test_status_update"},
        )

        self.assertRedirects(response, reverse("statuses:index"))
        status.refresh_from_db()
        self.assertEqual(status.name, "test_status_update")


class StatusDeleteViewTest(AuthenticatedTestCase):
    def test_delete_status(self):
        status = Status.objects.get(pk=1)
        response = self.client.post(
            reverse("statuses:delete", kwargs={"pk": status.pk}),
        )

        self.assertRedirects(response, reverse("statuses:index"))
        self.assertFalse(Status.objects.filter(pk=status.pk).exists())
