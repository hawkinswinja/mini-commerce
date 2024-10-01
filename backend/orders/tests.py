from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order
from unittest.mock import patch

class OrderCreationTests(TestCase):
    
    @patch('orders.signals.send_sms.send')  # Mock the send_sms function
    def test_send_sms_on_order_created(self, mock_send_sms):
        # Create a user and an order for the user
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        order = Order.objects.create(customer=user, product='Test Product', total=100.00)
        
        # Check if the signal was triggered and SMS was "sent"
        mock_send_sms.assert_called_once_with(['+254722123123'], f"Your Order for Test Product was successful with order id {order.order_id}.")

        # Optionally check that the order object was created
        self.assertEqual(Order.objects.count(), 1)
