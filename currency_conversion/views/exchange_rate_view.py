from django.db.models import Count, Q
from django.db.models.functions import Coalesce
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from currency_conversion.models import ExchangeRate
from currency_conversion.serializers.exchange_rate_serializer import ExchangeRateSerializer


class ExchangeRateView(ListAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    permission_classes = (permissions.IsAuthenticated,)
