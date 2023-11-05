from django.urls import include, path
from rest_framework import routers
from currency_conversion.views.currency import CurrencyView

router = routers.DefaultRouter()
router.register(r'currency', CurrencyView)

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
    # path('performance/<int:project_id>/user/<int:user_id>', UserPerforanceView.as_view()),
]
