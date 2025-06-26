from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# Account Manager for creating and managing user accounts
class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


# Custom User model
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


# Leak Report model with leak_type and created_at added
class LeakReport(models.Model):
    LEAK_CHOICES = [
        ('Pipe Burst', 'Pipe Burst'),
        ('Valve Failure', 'Valve Failure'),
        ('Illegal Connection', 'Illegal Connection'),
        ('Unknown', 'Unknown'),
    ]

    customer_name = models.CharField(max_length=100)
    leak_type = models.CharField(max_length=50, choices=LEAK_CHOICES, default='Unknown')
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Hii ndiyo itatumika kwenye admin.py

    def __str__(self):
        return f"{self.customer_name} - {self.leak_type} - {self.created_at}"