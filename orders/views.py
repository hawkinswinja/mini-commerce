from rest_framework import generics, permissions, viewsets
from .serializers import OrderSerializer
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
    """
    OrderViewSet API view for CRUD operations on Order objects.
    This view allows authenticated users to perform CRUD operations on their own orders.
    It uses the OrderSerializer for serialization and ensures that only authenticated users
    can access the view.
    Methods:
        get_queryset(self):
            Returns a queryset of orders filtered by the current authenticated user.
    Attributes:
        serializer_class (OrderSerializer): The serializer class used for the view.
        permission_classes (list): A list of permission classes that the user must pass to access the view.
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)