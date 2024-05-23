from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, rut, password=None, **extra_fields):
        if not rut:
            raise ValueError('El usuario debe tener un RUT')
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(rut, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    rut = models.IntegerField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.rut
