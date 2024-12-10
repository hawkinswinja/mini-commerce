from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
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


class OrderViewSetTestCase(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='johndoe', password='password123')

        # Create an authenticated API client
        self.client = APIClient()
        self.client.login(username='johndoe', password='password123')  # Log in the user

    def test_create_order(self):
        # Simulate an authenticated user creating an order
        data = {'product': 'Laptop', 'total': 1500.00}
        response = self.client.post(reverse('orders'), data)
        # Ensure the order is created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the created order belongs to the authenticated user
        order = Order.objects.get(order_id=response.data['order_id'])
        self.assertEqual(order.customer, self.user)
        self.assertEqual(order.product, 'Laptop')
        self.assertEqual(order.total, 1500.00)
