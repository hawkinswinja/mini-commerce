import random
from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(auto_now=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_item = models.CharField(max_length=255)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders')