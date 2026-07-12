from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BaseTestCase(TestCase):
    fixtures = ["users.json"]


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


class UserListViewTest(BaseTestCase):
    def test_users_page(self):
        response = self.client.get(reverse("users:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/index.html")


class UserCreateViewTest(BaseTestCase):
    def test_create_user(self):
        response = self.client.post(
            reverse("users:create"),
            {
                "first_name": "Ivan",
                "last_name": "Ivanov",
                "username": "ivan",
                "password1": "StrongPassword123",
                "password2": "StrongPassword123",
            },
        )

        self.assertRedirects(response, reverse("login"))
        self.assertTrue(User.objects.filter(username="ivan").exists())


class UserLoginViewTest(BaseTestCase):
    def test_login(self):
        response = self.client.post(
            reverse("login"),
            {
                "username": "admin",
                "password": "password123",
            },
        )

        self.assertRedirects(response, reverse("index"))


class UserUpdateViewTest(AuthenticatedTestCase):
    def test_update_user(self):
        response = self.client.post(
            reverse("users:update", args=[self.user.pk]),
            {
                "first_name": "Ivan666",
                "last_name": "Ivanov666",
                "username": "admin",
            },
        )

        self.assertRedirects(response, reverse("users:index"))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Ivan666")

    def test_update_another_user(self):
        other = User.objects.get(username="petrov")

        response = self.client.post(
            reverse("users:update", args=[other.pk]),
            {
                "first_name": "Hack",
                "last_name": "Hack",
                "username": "petrov",
            },
        )

        self.assertRedirects(response, reverse("users:index"))

        other.refresh_from_db()
        self.assertEqual(other.first_name, "Петр")


class UserDeleteViewTest(AuthenticatedTestCase):
    def test_delete_user(self):
        response = self.client.post(
            reverse(
                "users:delete",
                args=[self.user.pk],
            )
        )

        self.assertRedirects(response, reverse("users:index"))
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

    def test_delete_user_not_owner(self):
        other = User.objects.get(username="petrov")
        response = self.client.post(reverse("users:delete", args=[other.pk]))

        self.assertRedirects(response, reverse("users:index"))
        self.assertTrue(User.objects.filter(pk=other.pk).exists())
