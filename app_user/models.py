from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .usermanager import CustomUserManager
from .validators import validate_password_strength

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    auth_token_refresh = models.CharField(max_length=255, null=True, blank=True)
    auth_token_access = models.CharField(max_length=255, null=True, blank=True)
    
    username = models.CharField(max_length= 30, verbose_name="Имя",null=True, blank=True)
    surname = models.CharField(max_length= 30, verbose_name="Фамилия",null=True, blank=True)
    password = models.CharField("password",validators=[validate_password_strength], max_length=128)
    email_or_phone = models.CharField(max_length= 30,unique = True,null= True, blank=True)
    code = models.CharField(max_length=6, blank=True)
    created_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_usual = models.BooleanField(default=False)
    image = models.ImageField(upload_to='usual/profiles/')
    # number = models.CharField(max_length= 30,unique=True,null= True, blank=True)
    device_token = models.CharField(max_length = 100, verbose_name = 'токен от ios/android')

    objects = CustomUserManager()


    def __str__(self) -> str:
        return f"{self.username}"
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = verbose_name

    USERNAME_FIELD = 'email_or_phone'
    REQUIRED_FIELDS = ['username']


