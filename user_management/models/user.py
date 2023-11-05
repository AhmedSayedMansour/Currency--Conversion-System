from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import get_template
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import models



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserFunctions:
    """Define all the methods we need to add to the User class"""

    def tokens(self):
        """JWT token"""
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh),
                'access': str(refresh.access_token)}

    def activate(self):
        """Set the is_active to True"""
        self.is_active = True
        self.save()

    def generate_user_token(self):
        """Generate token for a user"""
        token = PasswordResetTokenGenerator()
        return token.make_token(self)

    def return_user_email_data(self, url):
        """Generate token and provide a url with credentials for user"""
        token = self.generate_user_token()
        uuid = urlsafe_base64_encode(force_bytes(self.pk))
        url = f'{url}'.replace('<uuid>', uuid).replace('<token>', token)
        return {'username': self.username, 'url': url}

    def send_activation_email(self):
        """send an html email for account activation"""
        html_template = get_template(f'emails/activate_account.html')
        ctx = self.return_user_email_data(settings.USER_EMAIL_ACTIVATION)
        html_content = html_template.render(ctx)
        self.email_user(
            'Activation Email',
            html_content,
            from_email=settings.EMAIL_HOST_USER)

    def send_reset_password_email(self):
        """send an html email for account reset_password"""
        html_template = get_template(f'emails/reset_password.html')
        ctx = self.return_user_email_data(settings.USER_PASSWORD_RESET)
        html_content = html_template.render(ctx)
        self.email_user(
            'Reset Password Email',
            html_content,
            from_email=settings.EMAIL_HOST_USER)

    def login_user_response(self):
        return {'user': {
            'email': self.email,
            # 'name': f'{self.first_name} {self.last_name}',
            'userName': self.username,
            'is_admin': self.is_superuser,
            # 'permissions': PermissionSerializer(
            #     authenticated_user.user_permissions.all(),
            #     many=True).data,
            # 'groups': GroupSerializer(
            #     self.groups.all(),
            #     many=True).data
        }, **self.tokens()
        }


# get_user_model().add_to_class('is_deleted', models.BooleanField(default=False))
# # Edit the USERNAME_FIELD field to not unique and make the email unique
# setattr(get_user_model(), 'USERNAME_FIELD', 'email')
# get_user_model()._meta.get_field('username')._unique = False
# get_user_model()._meta.get_field('username')._blank = True
# get_user_model()._meta.get_field('email')._unique = True
# get_user_model()._meta.get_field('email')._blank = False
# get_user_model()._meta.get_field('password')._blank = True
# setattr(get_user_model(), 'REQUIRED_FIELDS', [])

# Change the UserManager of the django auth User
get_user_model().add_to_class('objects', UserManager())

# add user function to an existing class
get_user_model().__bases__ += (UserFunctions,)
