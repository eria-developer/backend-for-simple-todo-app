from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True, verbose_name="groups")
    permissions = models.ManyToManyField(Permission, related_name="customuser_set", blank=True, verbose_name="permissions")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.username}"

    def user_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }