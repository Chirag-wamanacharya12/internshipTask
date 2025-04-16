from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Create and return a user with an email, username, and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and return a superuser with an email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = [
        ("admin", "admin"),
        ("viewer", "viewer"),
        ("guest", "Guest"),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="guest")
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    avatar = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Boolean flags to indicate whether the user is active
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # staff user
    is_superuser = models.BooleanField(default=False)  # superuser

    # Required fields
    REQUIRED_FIELDS = ['username', 'full_name']
    USERNAME_FIELD = 'email'  # Email is the unique identifier

    # Custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username