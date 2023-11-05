from currency_conversion.models import UserConversion
from django.utils import timezone
from datetime import timedelta

def update_status():
    now = timezone.now()
    time_threshold = now - timedelta(hours=48)
    objects_to_update = UserConversion.objects.filter(created_at__lte=time_threshold, status='temporary')
    for obj in objects_to_update:
        obj.status = 'permanent'
        obj.save()