from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'order_id': {'read_only': True},
            'created_at': {'read_only': True},
            'customer': {'read_only': True}
        }

