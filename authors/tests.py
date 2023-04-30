from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Author
from datetime import  date


class AuthorsTests(TestCase):
    def test_create_author(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo")
        author = Author.objects.create(first_name="f_name",
                                       second_name="s_name", 
                                       birth_at=date(2002,2,2),
                                       user=user
                                       )
        self.assertEqual(author.user.email, "normal@user.com")
        self.assertTrue(author.user.is_active)
        self.assertFalse(author.user.is_staff)
        self.assertFalse(author.user.is_superuser)

        self.assertEqual(author.first_name, "f_name")
        self.assertEqual(author.second_name, "s_name")
        self.assertEqual(author.birth_at, date(2002,2,2))
        self.assertEqual(author.user, user)
        



