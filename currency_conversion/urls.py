from django.urls import include, path
from rest_framework import routers
from currency_conversion.views.currency import CurrencyView
from currency_conversion.views.exchange_rate_view import ExchangeRateView
from currency_conversion.views.user_conversion_view import UserConversionView, CurrencyConvert

router = routers.DefaultRouter()
router.register(r'currency', CurrencyView)
# router.register(r'exchange_rate', ExchangeRateView)
# router.register(r'user_conversion', UserConversionView)

urlpatterns = [
    path(
        '',
        include(
            router.urls)),
    path('user_conversion', UserConversionView.as_view()),
    path('exchange_rate', ExchangeRateView.as_view()),
    path('convert', CurrencyConvert.as_view()),
]
