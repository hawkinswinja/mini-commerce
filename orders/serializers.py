from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'order_id': {'read_only': True},
            'order_time': {'read_only': True},
            'user_id': {'read_only': True}
        }

