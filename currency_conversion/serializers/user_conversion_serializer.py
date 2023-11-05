from rest_framework import serializers
from django.contrib.auth.models import User
# from user_management.serializers.auth import UserSerializer
from currency_conversion.models import UserConversion
from currency_conversion.utils.validators import validate_positive_non_zero


class UserConversionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserConversion
        fields = "__all__"
        read_only_fields = ["status", "result", "user", ]


class CurrencyConvertSerializer(serializers.Serializer):
    from_currency = serializers.CharField()
    to_currency = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=5, validators=[
                                      validate_positive_non_zero])
