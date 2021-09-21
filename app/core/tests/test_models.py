from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test Creating a new user with email"""
        email = "emaple@mail.com"
        password = "mb@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user_with_email_successfull(self):
        """Test Creating a new user with email"""
        email = "emaple@mail.com"
        password = "mb@123"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_not_anemail(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
        user=sample_user(),
        name='Vegan'
    )

        self.assertEqual(str(tag), tag.name)
