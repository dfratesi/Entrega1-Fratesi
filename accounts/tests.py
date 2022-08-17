from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="damian", email="damian@gmail.com", password="password123"
        )
        self.assertEqual(user.username, "damian")
        self.assertEqual(user.email, "damian@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="admin", email="superadmin@gmail.com", password="password123"
        )
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "superadmin@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
