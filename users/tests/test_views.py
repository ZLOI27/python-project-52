from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserListViewTest(TestCase):
    fixtures = ["users/tests/fixtures/users.json"]

    def test_users_page(self):
        response = self.client.get(reverse("users:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/index.html")


class UserCreateViewTest(TestCase):
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
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username="ivan").exists())


class LoginTest(TestCase):
    fixtures = ["users/tests/fixtures/users.json"]

    def test_login(self):
        response = self.client.post(
            reverse("login"),
            {
                "username": "admin",
                "password": "password123",
            },
        )

        self.assertRedirects(response, reverse("index"))


class UserUpdateViewTest(TestCase):
    fixtures = ["users/tests/fixtures/users.json"]

    def test_update_user(self):
        self.client.login(
            username="admin",
            password="password123",
        )

        user = User.objects.get(username="admin")

        response = self.client.post(
            reverse("users:update", args=[user.pk]),
            {
                "first_name": "Ivan666",
                "last_name": "Ivanov666",
                "username": "admin",
            },
        )

        self.assertRedirects(response, reverse("users:index"))

        user.refresh_from_db()
        self.assertEqual(user.first_name, "Ivan666")

    def test_update_another_user(self):
        self.client.login(
            username="admin",
            password="password123",
        )

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


class UserDeleteViewTest(TestCase):
    fixtures = ["users/tests/fixtures/users.json"]

    def test_delete_user(self):
        self.client.login(
            username="admin",
            password="password123",
        )

        user = User.objects.get(username="admin")
        response = self.client.post(reverse("users:delete", args=[user.pk]))

        self.assertRedirects(response, reverse("users:index"))
        self.assertFalse(User.objects.filter(pk=user.pk).exists())

    def test_delete_user_not_owner(self):
        self.client.login(
            username="admin",
            password="password123",
        )

        other = User.objects.get(username="petrov")
        response = self.client.post(reverse("users:delete", args=[other.pk]))

        self.assertRedirects(response, reverse("users:index"))

        other.refresh_from_db()
        self.assertTrue(User.objects.filter(pk=other.pk).exists())
