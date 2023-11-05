from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

# from .views.admin import (AddUserToGroupView, GroupViewSet, PermissionViewSet,
#                           RemoveUserFromGroupView, UserViewSet)
from .views.auth import (ActivateEmail, ChangePasswordTokenView,
                         ChangePasswordView, LoginView, RegistrationView,
                         ResetPassword, UserInfoView, EditUserView)

router = routers.DefaultRouter()
# router.register(r'groups', GroupViewSet)
# router.register(r'permissions', PermissionViewSet)
# router.register(r'user', UserViewSet)

urlpatterns = [
    path(
        '',
        include(router.urls)),
    path(
        'register',
        RegistrationView.as_view()),
    path(
        'login',
        LoginView.as_view()),
    path(
        'getuserinfo',
        UserInfoView.as_view()),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'activate/<uuid>/<token>/',
        ActivateEmail.as_view(),
        name='activate_account'),
    path(
        'reset_password/<uuid>/<token>/',
        ResetPassword.as_view(),
        name='reset_password'),
    path(
        'reset_password/',
        ResetPassword.as_view(),
        name='reset_password'),
    path(
        'change_password/',
        ChangePasswordView.as_view()),
    path(
        'change_password_token/',
        ChangePasswordTokenView.as_view()),
    # path(
    #     'groups/<int:group_id>/users/<int:user_id>//',
    #     AddUserToGroupView.as_view(),
    #     name='add-user-to-group'),
    # path(
    #     'groups/<int:group_id>/users/<int:user_id>/remove//',
    #     RemoveUserFromGroupView.as_view(),
    #     name='remove-user-from-group'),
    path('edit', EditUserView.as_view()),
]
