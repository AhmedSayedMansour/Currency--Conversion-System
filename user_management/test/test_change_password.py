import logging

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()
logger = logging.getLogger(__name__)


class ChangePasswordViewTestCase(APITestCase):
    def setUp(self):
        self.url = '/api/user/change_password/'
        self.data = {
            "old_password": "'password123'",
            "new_password": "string111",
            "confirm_new_password": "string111"
        }
        self.user = User.objects.create_user(
            email='user@example.com',
            username='user',
            password=self.data.get("old_password"))
        self.user.activate()
        self.token = AccessToken.for_user(self.user)

    def get_auth_header(self):
        return f'Bearer {self.token}'

    def authenticate_client(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_auth_header())

    def test_change_password_success(self):
        self.authenticate_client()
        response = self.client.patch(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logger.info(f'change password success response: {response.data}')

    def test_change_password_failure_invalid_new_password(self):
        self.data["new_password"] = '123'
        self.authenticate_client()
        response = self.client.patch(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.info(
            f'change password "old password is wrong" failed response: {response.data}')

    def test_change_password_failure_wrong_old_password(self):
        self.data["old_password"] = '123'
        self.authenticate_client()
        response = self.client.patch(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.info(
            f'change password "old password is wrong" failed response: {response.data}')

    def test_change_password_failure_invalid_new_password(self):
        self.data["new_password"] = '123'
        self.authenticate_client()
        response = self.client.patch(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.info(
            f'change password "invalid new password" failed response: {response.data}')

    def test_change_password_failure_new_password_mismatch(self):
        self.data["confirm_new_password"] += '$'
        self.authenticate_client()
        response = self.client.patch(self.url, self.data, 'json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.info(
            f'change password "new password mismatch" failed response: {response.data}')
