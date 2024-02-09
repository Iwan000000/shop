from django.contrib.auth.models import AbstractUser
from django.db import models

from shoping.models import NULLABLE


# Create your models here.


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    is_verified = models.BooleanField(default=False, verbose_name='подтвержден ли аккаунт')
    verification_token = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="avatar/", **NULLABLE, verbose_name='аватар')
    phone_number = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    country = models.CharField(max_length=100, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
