"""
Tests for User Api endpoints
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class PublicUserApiTests(TestCase):
    """Test for public user api's"""

    def setUp(self):
        self.client = APIClient()
        self.data = {
            'email': 'test@example.com',
            'password': 'mrshanas',
            'username': 'testuser'
        }

    def test_user_created_success(self):
        """Test for creating users in the db"""

        res = self.client.post(reverse('users:create'), self.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_created_with_unique_email(self):
        """Test if a user created with existing email fails"""
        user = get_user_model().objects.create_user(**self.data)
        res = self.client.post(reverse('users:create'), self.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(get_user_model().objects.filter(
            email=user.email).exists())
