from django.db import models
from django.contrib.auth.models import (
  AbstractUser, BaseUserManager
)


class CustomUserManager(BaseUserManager):
  
  def create_user(self, username, email, password, **extra_fields):
    if not username:
      raise ValueError('The username must be set')
    if not email:
      raise ValueError('The email must be set')
    
    user = self.model(
      username=username,
      email=self.normalize_email(email),
      **extra_fields
    )

    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, username, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_stuff=True')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True')
    if extra_fields.get('is_active') is not True:
      raise ValueError('Superuser must have is_active=True')
    
    return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
  username = models.CharField(max_length=25, unique=True)
  email = models.EmailField(max_length=255, unique=True)

  objects = CustomUserManager()
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email']
