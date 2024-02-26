# Importar los módulos necesarios de Django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)

# Crear un administrador personalizado para el modelo CustomUser
class CustomUserManager(UserManager):
    # Método privado para crear un usuario con el email, contraseña y campos adicionales especificados
    def _create_user(self, email, password, **extra_fields):
        # Verificar si se proporcionó un email, lanzar un error si no
        if not email:
            raise ValueError('El campo Email debe ser establecido')
        
        # Normalizar la dirección de email
        email = self.normalize_email(email)
        
        # Crear una nueva instancia de usuario con el email proporcionado y campos adicionales
        user = self.model(email=email, **extra_fields)
        
        # Establecer la contraseña para el usuario
        user.set_password(password)
        
        # Guardar el usuario en la base de datos
        user.save(using=self._db)
        
        # Devolver el usuario creado
        return user

    # Método público para crear un usuario regular con el valor predeterminado 'is_staff' establecido en False
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)
    
    # Método público para crear un usuario del personal con el valor 'is_staff' establecido en True
    def create_staffuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

# Modelo de Usuario personalizado que hereda de AbstractBaseUser y PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    # Campos para el modelo de Usuario
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    avatar = models.ImageField(default="avatar.png")
    data_joined = models.DateTimeField(default=timezone.now)
    staff = models.BooleanField(default=False)
    
    # Administrador personalizado para el modelo de Usuario
    objects = CustomUserManager()
    
    # Especificar el campo 'email' como el campo de nombre de usuario para la autenticación
    USERNAME_FIELD = 'email'
    
    # No hay campos adicionales requeridos para la creación de usuario
    REQUIRED_FIELDS = []
    
    # Clase Meta para definir el ordenamiento del modelo de Usuario basado en 'data_joined'
    class Meta:
        ordering = ['data_joined']

# Create your models here.
