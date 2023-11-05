from django.db.models import Count, Q
from django.db.models.functions import Coalesce
from rest_framework import permissions, viewsets
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView, CreateAPIView)
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import action

from django.contrib.auth.models import User
from currency_conversion.models import UserConversion, ExchangeRate
from currency_conversion.serializers.user_conversion_serializer import UserConversionSerilizer, CurrencyConvertSerializer


class UserConversionView(ListAPIView):
    queryset = UserConversion.objects.all()
    serializer_class = UserConversionSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class CurrencyConvert(CreateAPIView):
    queryset = UserConversion.objects.all()
    serializer_class = CurrencyConvertSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        from_currency = self.request.data["from_currency"]
        to_currency = self.request.data["to_currency"]
        amount = self.request.data["amount"]

        rate = ExchangeRate.objects.filter(from_currency__code=from_currency, to_currency__code=to_currency).first()
        if rate :
            result = int(amount) * int(rate.exchange_rate)
            user_convert = UserConversion.objects.create(user=self.request.user, amt=amount, rate=rate, result=result)
            return Response(UserConversionSerilizer(user_convert).data)
        else:
            return Response("exchange rate does not exist")
