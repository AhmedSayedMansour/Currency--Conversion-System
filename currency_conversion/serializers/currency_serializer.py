from rest_framework import serializers
from django.contrib.auth.models import User
# from user_management.serializers.auth import UserSerializer
from currency_conversion.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"
