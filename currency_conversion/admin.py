from django.contrib import admin
from .models.currency import Currency
from .models.exchange_rate import ExchangeRate
from .models.user_conversion import UserConversion

# Register your models here.
admin.site.register(Currency)
admin.site.register(ExchangeRate)
admin.site.register(UserConversion)
