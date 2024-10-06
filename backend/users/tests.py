from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Customer


User = get_user_model()


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


# Test CSRF token retrieval
class CSRFTests(TestCase):
    def test_get_csrf_token(self):
        response = self.client.get(reverse('get_csrf'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('csrftoken', response.json())


# Test authentication check
class AuthenticationTests(TestCase):
    def test_unauthenticated_check(self):
        response = self.client.get(reverse('is_authenticated'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['authenticated'])

    def test_authenticated_check(self):
        User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('is_authenticated'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['authenticated'])


# Test login functionality
class LoginViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('user_login')

    def test_login_successful(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, 'Logged in successfully')

    def test_login_failure(self):
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, 400)
