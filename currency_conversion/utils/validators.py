from django.core.exceptions import ValidationError


def validate_positive_non_zero(value):
    if value <= 0:
        raise ValidationError("positive non-zero values only.")
