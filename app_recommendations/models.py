from django.db import models
from product.models import Product

class Recommendations(models.Model):
    product = models.ManyToManyField(Product)