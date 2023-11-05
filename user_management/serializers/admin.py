# from django.contrib.auth.models import Group, Permission, User
# from rest_framework import serializers


# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         # fields = ['url', 'name']
#         fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         # fields = ['url', 'name']
#         fields = ['id', 'username', 'email', 'is_active', 'date_joined']


# class GroupSerializer(serializers.ModelSerializer):
#     # Use PermissionSerializer for GET
#     permissions = PermissionSerializer(many=True, read_only=True)
#     # Accept a list of permissions IDs in the POST request
#     permissions_list = serializers.ListField(
#         child=serializers.JSONField(), write_only=True)

#     class Meta:
#         model = Group
#         fields = ["id", "name", "permissions", "permissions_list"]

#     def update(self, instance, validated_data):
#         permissions = validated_data.pop('permissions_list', [])
#         instance.permissions.set([obj.get('id') for obj in permissions])
#         return super().update(instance, validated_data)

#     def create(self, validated_data):
#         permissions = validated_data.pop('permissions_list', [])
#         group = Group.objects.create(**validated_data)

#         for permission in permissions:
#             permission_instance = Permission.objects.get(
#                 pk=permission.get('id'))
#             group.permissions.add(permission_instance)

#         return group
