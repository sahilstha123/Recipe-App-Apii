from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,  # Base class for creating custom user models
    PermissionsMixin,  # Adds permission-related fields and methods
    BaseUserManager    # A helper class for creating custom user managers
)


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('user must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    # This tells Django to use the email as the unique field for
    #  authentication instead of the default "username".
    USERNAME_FIELD = 'email'
