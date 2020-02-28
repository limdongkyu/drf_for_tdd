from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password", "date_joined")

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("입력한 패스워드들이 틀려요.")
        del attrs['confirm_password']
        attrs['password'] = make_password(attrs['password'])
        return attrs


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': '당신 계정은 비활성화.',
        'invalid_credentials': '당신은 자격이 없는 사용자.'
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')
    
    default_error_messages = {
        'inactive_account': '당신 계정은 비활성화.',
        'invalid_credentials': '당신은 자격이 없는 사용자.'
    }
    
    class Meta:
        model = Token
        fields = ("auth_token", "created")
    
    def validate(self, attrs):
        
        try:
            token = attrs.get("key")
            user = Token.objects.get(key=token).user
        except ObjectDoesNotExist:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])

        if not user.is_active:
            raise serializers.ValidationError(self.error_messages['inactive_account'])
        
        return attrs
