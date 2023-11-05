from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path(
        '',
        include(
            router.urls)),
    # path(
    #     'project/<project_id>/stat/',
    #     ProjectStat.as_view()),
    # path(
    #     'list/<int:organization_id>',
    #     GetProjectsByOrganizationView.as_view()),
    # path('performance/<int:project_id>', ProjectPerformanceView.as_view()),
    # path('performance/<int:project_id>/user/<int:user_id>', UserPerforanceView.as_view()),
]
