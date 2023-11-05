from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from currency_conversion.utils.validators import validate_positive_non_zero


class UserConversion(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    amt = models.DecimalField(max_digits=10,
                              decimal_places=6, validators=[validate_positive_non_zero])

    rate = models.ForeignKey("currency_conversion.ExchangeRate", verbose_name=_(
        "Convertion_Rate"), on_delete=models.DO_NOTHING)

    status_choices = (
        ('temporary', 'temporary'),
        ('permanent', 'permanent'),
    )
    status = models.CharField(
        choices=status_choices,
        default="temporary",
        max_length=10
    )

    result = models.IntegerField()

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.user.username + "_" + str(self.created_at)
