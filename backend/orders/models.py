import random
from django.db import models


# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    product = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')
