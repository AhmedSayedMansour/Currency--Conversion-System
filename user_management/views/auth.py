from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response

from user_management.serializers.auth import (ChangePasswordSerializer,
                                              ChangePasswordTokenSerializer,
                                              LoginSerializer,
                                              RegistrationSerializer,
                                              UserSerializer)


class ActivateEmail(GenericAPIView):
    """Activate account using the token generated and user id"""

    def get(self, request, uuid, token):
        # get user_id from uuid and get the object using the User model
        user_id = force_str(urlsafe_base64_decode(uuid))
        user = User.objects.filter(pk=user_id).first()

        # check if the token is authorized
        if user and PasswordResetTokenGenerator().check_token(user, token):
            # Activate the account
            user.activate()
            return HttpResponse('Account activated successfully')
        elif user:
            user.send_activation_email()
            return HttpResponse('resend activation mail')
        return HttpResponse('Activation Failed')


class ResetPassword(GenericAPIView):
    """Reset Password using the token generated and user id"""

    def post(self, request, uuid, token):
        """Reset user password authenticated by his user token and uid"""

        # get user_id from uuid and get the object using the User model
        user_id = force_str(urlsafe_base64_decode(uuid))
        user = User.objects.filter(pk=user_id).first()
        tokenObj = PasswordResetTokenGenerator()

        # TODO replace with Serializer
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if user and tokenObj.check_token(user, token):
            if any(new_password and confirm_new_password) == False:
                return HttpResponse('passwords can not be none or empty')
            elif new_password != confirm_new_password:
                return HttpResponse('both passwords are different')
            # Reset Password
            user.set_password(new_password)
            user.save()
            return HttpResponse('success')
        user.send_reset_password_email()
        return HttpResponse(
            'token not valid, we have sent new reset password credentials')

    def get(self, request):
        """send reset password email by his email"""

        email = request.GET.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            user.send_reset_password_email()
            return HttpResponse('send')
        else:
            return HttpResponse('email not found')


class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        api to register new users
        request body:
            first_name
            last_name
            email
            password
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response(data, status=status.HTTP_200_OK)


class UserInfoView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(request.user.login_user_response())


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.none()

    def get_object(self, queryset=None):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        # user = self.get_object()
        user = User.objects.get(email=request.data.get("email"))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Check old password
        # if not user.check_password(request.data.get("old_password")):
        #     return Response(
        #         {"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        # confirm the new passwords match
        if request.data.get("new_password") != request.data.get(
                "confirm_new_password"):
            return Response({"new_password": [
                "New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)
        # set_password also hashes the password that the user will get
        user.set_password(request.data.get("new_password"))
        user.save()
        return Response(
            {"response": "successfully changed password"}, status=status.HTTP_200_OK)


class ChangePasswordTokenView(GenericAPIView):
    serializer_class = ChangePasswordTokenSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        serializer = self.get_serializer(data=request.data, context={'email': user.email})
        serializer.is_valid(raise_exception=True)
        # Check old password
        # if not user.check_password(request.data.get("old_password")):
        #     return Response(
        #         {"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        # confirm the new passwords match
        if request.data.get("new_password") != request.data.get(
                "confirm_new_password"):
            return Response({"new_password": [
                "New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)
        # set_password also hashes the password that the user will get
        user.set_password(request.data.get("new_password"))
        user.save()
        return Response(
            {"response": "successfully changed password"}, status=status.HTTP_200_OK)


class EditUserView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user