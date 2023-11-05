from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency_conversion'

    def ready(self):
        from django_q.tasks import schedule
        from django.utils import timezone
        from datetime import timedelta
        # Ensure you don't schedule tasks more than once: check if the task is already scheduled
        # Schedule your task using Django-Q's schedule function
        schedule('currency_conversion.tasks.update_status',
                 schedule_type='I',
                 minutes=30,
                 next_run=timezone.now()  # This is optional
                 )

