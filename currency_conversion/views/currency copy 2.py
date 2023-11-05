from django.db.models import Count, Q
from django.db.models.functions import Coalesce
from rest_framework import permissions, viewsets
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.response import Response

from django.contrib.auth.models import User
from currency_conversion.models import Currency
from currency_conversion.serializers.currency_serializer import CurrencySerializer


class CurrencyListView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


# class ProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [permissions.DjangoModelPermissions]

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             queryset = Project.objects.all()
#         else:
#             queryset = Project.objects.filter(
#                 Q(
#                     created_by=self.request.user) | Q(
#                     organization__created_by=self.request.user) | Q(
#                     organization__in=OrganizationMember.objects.filter(
#                         user=self.request.user).values_list(
#                         'organization_id',
#                         flat=True)))
#         return queryset.prefetch_related('tasks').annotate(
#             labelled=Coalesce(
#                 Count('tasks', filter=Q(tasks__state='labelled')),
#                 0),
#             under_review=Coalesce(
#                 Count('tasks', filter=Q(tasks__state='under_review')),
#                 0),
#             assigned=Coalesce(
#                 Count('tasks', filter=Q(tasks__state='assigned')),
#                 0),
#             pending=Coalesce(
#                 Count('tasks', filter=Q(tasks__state='pending')),
#                 0),
#             unassigned=Coalesce(
#                 Count('tasks', filter=Q(tasks__state='unassigned')),
#                 0)
#         )

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return ProjectStatsSerializer
#         return self.serializer_class

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)


class CurrencyConvertView(GenericAPIView):
    def get(self, request, project_id):
        project = Project.objects.filter(pk=project_id).first()
        stat = project.get_stat
        return Response(stat)
