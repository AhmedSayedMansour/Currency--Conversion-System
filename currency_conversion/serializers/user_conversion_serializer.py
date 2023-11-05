from rest_framework import serializers
from django.contrib.auth.models import User
# from user_management.serializers.auth import UserSerializer
from currency_conversion.models import UserConversion


class UserConversionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserConversion
        fields = "__all__"
