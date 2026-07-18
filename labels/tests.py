from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from labels.models import Label


class BaseTestCase(TestCase):
    fixtures = [
        "users.json",
        "statuses.json",
        "labels.json",
        "tasks.json",
    ]
    t_name = ""
    t_username = "admin"
    t_password = "zxcvbn12"


class AuthenticatedTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.get(username=self.t_username)
        self.assertTrue(
            self.client.login(
                username=self.t_username,
                password=self.t_password,
            )
        )


class LabelListViewTest(AuthenticatedTestCase):
    def test_label_list(self):
        response = self.client.get(reverse("labels:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "labels/index.html")


class LabelCreateViewTest(AuthenticatedTestCase):
    def test_create_label(self):
        response = self.client.post(
            reverse("labels:create"),
            {
                "name": "New label",
            },
        )

        self.assertRedirects(response, reverse("labels:index"))
        self.assertTrue(Label.objects.filter(name="New label").exists())


class LabelUpdateViewTest(AuthenticatedTestCase):
    def test_update_label(self):
        label = Label.objects.get(pk=1)

        response = self.client.post(
            reverse("labels:update", args=[label.pk]),
            {
                "name": "Updated label",
            },
        )

        self.assertRedirects(response, reverse("labels:index"))

        label.refresh_from_db()
        self.assertEqual(label.name, "Updated label")


class LabelDeleteViewTest(AuthenticatedTestCase):
    def test_delete_label(self):
        label = Label.objects.get(pk=3)

        response = self.client.post(
            reverse("labels:delete", args=[label.pk]),
        )

        self.assertRedirects(response, reverse("labels:index"))
        self.assertFalse(Label.objects.filter(pk=label.pk).exists())

    def test_delete_label_in_use(self):
        label = Label.objects.get(pk=1)

        response = self.client.post(
            reverse("labels:delete", args=[label.pk]),
        )

        self.assertRedirects(response, reverse("labels:index"))
        self.assertTrue(Label.objects.filter(pk=label.pk).exists())


class LabelAccessTest(BaseTestCase):
    def test_guest_cannot_open_label_list(self):
        response = self.client.get(reverse("labels:index"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('labels:index')}",
        )
