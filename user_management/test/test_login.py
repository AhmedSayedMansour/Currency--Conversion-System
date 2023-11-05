import logging

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()
logger = logging.getLogger(__name__)


class LoginViewTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(
            email='user@example.com',
            username='user',
            password='password123').activate()
        self.url = '/api/user/login'
        self.data = {
            'email': 'user@example.com',
            'password': 'password123'
        }

    def test_login_success(self):
        response = self.client.post(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['user']['email'], 'user@example.com')
        logger.info(f'login success response: {response.data}')

    def test_login_failure(self):
        self.data['email'] = 'invalidemail'
        response = self.client.post(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.info(f'login failed response: {response.data}')
