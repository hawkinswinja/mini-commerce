from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .sms import send_sms

@receiver(post_save, sender=Order)
def send_sms_for_order_created(sender, instance, created, **kwargs):
    if created:
        # recipient = instance.phone
        recipient = '+254722123123'
        message = f"Your Order for {instance.product} was successful with order id {instance.order_id}."
        send_sms.send([recipient], message)
        