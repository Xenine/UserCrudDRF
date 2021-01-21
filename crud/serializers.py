from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_superuser",
            "date_joined",
            "password",
        ]
        extra_kwargs = {'password': {'write_only': True},
                        'id': {'read_only': True},
                        'is_superuser': {'read_only': True}, 
                        'date_joined': {'read_only': True}}