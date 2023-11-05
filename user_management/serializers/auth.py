from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(list(e))
        return value

    def save(self):
        user = User.objects.create_user(**self.validated_data)
        user.activate()
        return user

    def to_representation(self, instance):
        """Modify the representation format."""
        representation = super().to_representation(instance)
        representation['user'] = representation.copy()
        return representation


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        user = User.objects.filter(username=data.get('username')).first()
        if user:
            if user.is_active:
                authenticated_user = authenticate(
                    username=data.get('username'),
                    password=data.get('password'))
                if authenticated_user:
                    return {
                        **authenticated_user.login_user_response(),
                        # 'permissions': PermissionSerializer(
                        #     authenticated_user.user_permissions.all(),
                        #     many=True).data,
                        # 'groups': GroupSerializer(
                        #     authenticated_user.groups.all(),
                        #     many=True).data
                    }
            else:
                user.send_activation_email()
                raise serializers.ValidationError(
                    {"error": "please verify your email"}
                )
        raise serializers.ValidationError(
            {"error": "Email or Password you entered is incorrect"}
        )


class ChangePasswordSerializer(serializers.Serializer):
    # old_password = serializers.CharField(
    #     required=True, style={
    #         'input_type': 'password'}, write_only=True)
    email = serializers.CharField(
        required=True, style={
            'input_type': 'email'}, write_only=True)
    new_password = serializers.CharField(
        required=True, style={
            'input_type': 'password'}, write_only=True)
    confirm_new_password = serializers.CharField(
        required=True, style={
            'input_type': 'password'}, write_only=True)

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(list(e))
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'is_active', 'date_joined']
        read_only_fields = ['id', 'is_active', 'date_joined']


class ChangePasswordTokenSerializer(serializers.Serializer):
    # old_password = serializers.CharField(
    #     required=True, style={
    #         'input_type': 'password'}, write_only=True)
    # email = serializers.CharField(
    #     required=True, style={
    #         'input_type': 'email'}, write_only=True)
    new_password = serializers.CharField(
        required=True, style={
            'input_type': 'password'}, write_only=True)
    confirm_new_password = serializers.CharField(
        required=True, style={
            'input_type': 'password'}, write_only=True)

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(list(e))
        if authenticate(username=self.context.get('email'), password=value):
            raise serializers.ValidationError(
                "Your new password cannot be the same as your old password."
            )
        return value
