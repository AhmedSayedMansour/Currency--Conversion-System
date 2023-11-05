from django.db.models import Count, Q
from django.db.models.functions import Coalesce
from rest_framework import permissions, viewsets
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView, ListCreateAPIView)
from currency_conversion.models import Currency
from currency_conversion.serializers.currency_serializer import CurrencySerializer


class CurrencyView(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
