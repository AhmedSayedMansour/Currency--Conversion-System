from rest_framework import serializers
from django.contrib.auth.models import User
from user_management.serializers.auth import UserSerializer


# class ProjectSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True, allow_null=True)

#     class Meta:
#         model = Project
#         fields = '__all__'
#         # read_only_fields = ['created_by']


# class ProjectStatsSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True, allow_null=True)
#     unassigned = serializers.IntegerField(default=0)
#     pending = serializers.IntegerField(default=0)
#     assigned = serializers.IntegerField(default=0)
#     under_review = serializers.IntegerField(default=0)
#     labelled = serializers.IntegerField(default=0)

#     class Meta:
#         model = Project
#         fields = '__all__'


# class ProjectPerformanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ['id', 'project_performance']


# class UserPerformanceSerializer(serializers.ModelSerializer):
#     # user = UserSerializer(read_only=True, allow_null=True)
#     class Meta:
#         model = Project
#         fields = ['id', 'user_performance']
