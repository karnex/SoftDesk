from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self, request, *args, **kwargs):
        user = User(last_name=self.validated_data['last_name'], first_name=self.validated_data['first_name'],
                    email=self.validated_data['email'], username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class UserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PasswordSerializer(serializers.Serializer):
    """ Serializer change for password change endpoint """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
