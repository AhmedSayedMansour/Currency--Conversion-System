from django.db import models
from django.utils.translation import gettext_lazy as _
from currency_conversion.utils.validators import validate_positive_non_zero


class ExchangeRate(models.Model):

    from_currency = models.ForeignKey("currency_conversion.Currency", verbose_name=_(
        "from_currency"), on_delete=models.DO_NOTHING, related_name="from_currency")
    to_currency = models.ForeignKey("currency_conversion.Currency", verbose_name=_(
        "to_currency"), on_delete=models.DO_NOTHING, related_name="to_currency")

    exchange_rate = models.DecimalField(
        max_digits=10, decimal_places=6, validators=[validate_positive_non_zero])

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["from_currency"]),
            models.Index(fields=["to_currency"]),
            models.Index(fields=["from_currency", "to_currency"]),
        ]

    def __str__(self):
        return self.from_currency.code + "_" + self.to_currency.code + "_" + str(self.created_at)
