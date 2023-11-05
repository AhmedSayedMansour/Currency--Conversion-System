from rest_framework import serializers
from django.contrib.auth.models import User
# from user_management.serializers.auth import UserSerializer
from currency_conversion.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = "__all__"
