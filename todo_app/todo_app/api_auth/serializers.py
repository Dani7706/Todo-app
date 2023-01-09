from django.contrib.auth import password_validation, get_user_model
from django.core import exceptions
from rest_framework import serializers

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user

    def validate(self, attrs):
        user = UserModel(**attrs)
        password = user.password
        errors = {}
        try:
            password_validation.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(attrs)

    def to_representation(self, instance):
        user_repr = super().to_representation(instance)
        user_repr.pop('password')
        return user_repr
