from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer

class OIDCAuthTests(TestCase):

    def test_oidc_login_view(self):
        """
        Test that the login view for OIDC is working and returns the correct redirect.
        """
        response = self.client.get(reverse('oidc_authentication_init'))
        self.assertEqual(response.status_code, 302)  # Redirect to OIDC provider

        # Check that the URL points to the OIDC provider login
        self.assertIn('scope=openid', response['Location'])

class CustomerCreationTests(TestCase):
    """
    Test that a Customer object is created automatically when a User object is created.
    """
    
    def test_create_customer_on_user_signup(self):
        # Create a user
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')

        # Check if the Customer object is created automatically
        customer = Customer.objects.get(user=user)
        self.assertEqual(customer.name, 'testuser@example.com')