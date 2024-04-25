from django.db import models
from product.models import Product
from django.utils import timezone




class Vip(models.Model):
    icon = models.ImageField(upload_to='vip/')
    product = models.ManyToManyField(Product)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        indexes = [
            models.Index(fields=['id'])
        ]

