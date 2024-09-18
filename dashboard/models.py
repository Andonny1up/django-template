"""Modelos de la aplicación dashboard."""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission
)
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    """Manager para el modelo User."""

    def create_user(self, email, password=None, **extra_fields):
        """Crea y guarda un usuario con el email y contraseña proporcionados."""
        if not email:
            raise ValueError('El email debe ser proporcionado')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Crea y guarda un superusuario con el email y contraseña proporcionados."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
        Modelo de usuario personalizado que soporta el uso de email en lugar de username.
        Incluye una foto de perfil y campos requeridos para un usuario de Django.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        Group, related_name='dashboard_user_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='dashboard_user_set', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self


# Menu for the dashboard
class Menu(models.Model):
    """ Modelo para gestionar el menú del panel de control. """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    

class MenuItem(models.Model):
    """ Modelo para gestionar los elementos del menú del panel de control. """
    menu = models.ForeignKey(Menu, related_name="items" ,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name="children", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=0)
    is_dynamic = models.BooleanField(default=False)
    target = models.CharField(
        max_length=10,
        choices=[('_self', 'Misma pantalla'), ('_blank', 'Nueva pantalla')],
        default='_self'
    )


    def __str__(self) -> str:
        return self.name