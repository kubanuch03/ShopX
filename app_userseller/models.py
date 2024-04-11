from django.db import models
from app_user.models import CustomUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from .validators import validate_password_strength

from .sellermanager import CustomSellerManager
class SellerProfile(AbstractBaseUser, PermissionsMixin):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller_profile',blank=True,null=True)

    username = models.CharField(max_length= 30, verbose_name="Имя",null=True, blank=True)
    surname = models.CharField(max_length= 30, verbose_name="Фамилия",null=True, blank=True)
    password = models.CharField("password",validators=[validate_password_strength], max_length=128)
    email_or_phone = models.CharField(max_length= 30,unique = True,null= True, blank=True)
    code = models.CharField(max_length=6, blank=True)
    shop_name = models.CharField(max_length=255,blank=True,null=True)

    is_active = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    image = models.ImageField(upload_to='seller/profiles/')
    category_sc= models.ForeignKey('CategorySC',on_delete=models.CASCADE,blank=True,null=True)
    address = models.CharField(max_length = 50)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    device_token = models.CharField(max_length = 100, verbose_name = 'токен от ios/android')

    instagram_link = models.URLField(null=True, blank=True)
    whatsapp_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)


    objects = CustomSellerManager()
    USERNAME_FIELD = 'email_or_phone'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name='customuser_set',  # Измененное имя обратной связи
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',  # Измененное имя обратной связи
        related_query_name='user',
    )

    def __str__(self) -> str:
        return f'Seller {self.email_or_phone}'
    
    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = verbose_name



class CategorySC(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"