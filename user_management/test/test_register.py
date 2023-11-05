import logging

from rest_framework import status
from rest_framework.test import APITestCase

logger = logging.getLogger(__name__)


class RegistrationViewTestCase(APITestCase):
    def setUp(self):
        self.url = '/api/user/register'
        self.data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password': 'password123'
        }

    def test_registration_success(self):
        response = self.client.post(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')
        self.assertEqual(response.data['last_name'], 'Doe')
        self.assertEqual(response.data['email'], 'johndoe@example.com')
        logger.info(f'registration success response: {response.data}')

    def test_registration_failure(self):
        self.data['email'] = 'invalidemail'
        response = self.client.post(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
