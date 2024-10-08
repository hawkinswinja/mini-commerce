from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.customer_name
