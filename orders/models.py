import uuid
from django.db import models

# Create your models here.
class Order:
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    