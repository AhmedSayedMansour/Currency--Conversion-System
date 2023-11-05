from django.contrib.contenttypes.models import ContentType

from organizations.models import OrganizationMember


def group_has_admin_permission(instance):
    content_type = ContentType.objects.get_for_model(OrganizationMember)
    return instance.permissions.filter(
        codename='admin', content_type=content_type).exists()
