from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from common.abstact import AbstractCreatedModel, AbstractUpdatedModel
from common.constants import ROLES


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    def create_staff(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Нужен email")
        if not password:
            raise ValueError("Нужен пароль")

        email = self.normalize_email(email)
        user = self.model(email=email,
                          **extra_fields)

        user.set_password(password)

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractCreatedModel, AbstractUpdatedModel):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(choices=ROLES, max_length=64, default='Guest')
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return ' '.join(self.name, self.surname)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class UserProfile(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='profile', verbose_name="profile image")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=4096) 