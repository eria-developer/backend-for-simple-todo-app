from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=254, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=254, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "username", "password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password", "")
        password2 = attrs.get("password2", "")
        if password != password2:
            raise serializers.ValidationError("Passwords should match")
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "access_token", "refresh_token"]

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        request = self.context.get("request")
        print(f"Attributes {attrs}" )

        user = authenticate(request, email=email, password=password)

        if not user:
            raise serializers.ValidationError("Email or password is wrong")
        
        user_tokens = user.user_tokens()

        return {
            "Message": "User login successfull",
            "Email": user.email,
            # "Username": user.username,
            "Access Token": str(user_tokens.get("access")),
            "Refresh Token": str(user_tokens.get("refresh"))
        }