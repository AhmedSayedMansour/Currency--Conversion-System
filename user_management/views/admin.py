# from django.contrib.auth.models import Group, Permission, User
# from rest_framework import permissions, viewsets, mixins
# from rest_framework.views import APIView

# from user_management.serializers.admin import (GroupSerializer,
#                                                PermissionSerializer,
#                                                UserSerializer)


# class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = User.objects.filter(is_active=False)
#     serializer_class = UserSerializer
#     permission_classes = [permissions.DjangoModelPermissions]

#     def perform_destroy(self, instance):
#         instance.is_deleted = True
#         instance.is_active = False
#         instance.save(update_fields=['is_active'])



# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.DjangoModelPermissions]


# class PermissionViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Permission.objects.all()
#     serializer_class = PermissionSerializer
#     permission_classes = [permissions.DjangoModelPermissions]


# class AddUserToGroupView(APIView):

#     def get_group(self, group_id):
#         try:
#             return Group.objects.get(id=group_id)
#         except Group.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return None

#     def put(self, request, group_id, user_id):
#         group = self.get_group(group_id)
#         user = self.get_user(user_id)
#         if group and user:
#             group.user_set.add(user)
#             return Response({'message': 'User added to group successfully.'})
#         else:
#             return Response({'error': 'Group or user not found.'},
#                             status=status.HTTP_404_NOT_FOUND)


# class RemoveUserFromGroupView(APIView):

#     def get_group(self, group_id):
#         try:
#             return Group.objects.get(id=group_id)
#         except Group.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return None

#     def put(self, request, group_id, user_id):
#         group = self.get_group(group_id)
#         user = self.get_user(user_id)
#         if group and user:
#             group.user_set.remove(user)
#             return Response(
#                 {'message': 'User removed from group successfully.'})
#         else:
#             return Response({'error': 'Group or user not found.'},
#                             status=status.HTTP_404_NOT_FOUND)
