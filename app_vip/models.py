from django.db import models
from product.models import Product

class Vip(models.Model):
    product = models.ManyToManyField(Product)