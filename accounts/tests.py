from django.test import TestCase, Client

# Create your tests here.
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from datetime import timedelta
from django.utils import timezone
from .models import ResetPasswordToken


class BaseAPITest(APITestCase):
    def setUp(self, password=None) -> None:
        self.user = User(username="John Smith", email="john@example.com")
        self.user.set_password("123")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def user_factory(self, username="peter", email="peter@example.com", password="123"):
        user = User(username=username, email=email, password=password)
        user.save()
        return user


class ResetPasswordAPITest(BaseAPITest):
    def test_request_password_with_no_settings(self):
        # make sure that if no setting, the default password request reset field is the email.
        user = self.user_factory()
        data = {"email": user.username}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 400)

        data = {"email": user.email}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

    def test_request_password_with_django_rest_lookup_field_setting(self):
        # Make sure we can still use DJANGO_REST_LOOKUP_FIELD  setting for backward compatibility.
        settings.DJANGO_REST_LOOKUP_FIELD = "username"
        user = self.user_factory()
        data = {"email": user.username}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

    def test_request_password_with_django_rest_lookup_fields_setting(self):
        # Make sure new users can use  DJANGO_REST_LOOKUP_FIELDS  setting.
        settings.DJANGO_REST_LOOKUP_FIELDS = ["email", "username"]
        user = self.user_factory()
        data = {"email": user.username}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

        data = {"email": user.email}
        response = self.client.post(reverse("reset-password-request"), data=data)
        self.assertEqual(response.status_code, 200)
        msg = "A password reset token has been sent to the provided email address"
        self.assertEqual(response.data["message"], msg)

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_login_view(self):
        response = self.client.post(reverse('profile:login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirected after successful login

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile:logout'))
        self.assertEqual(response.status_code, 302)  # Redirected after logout

    def test_signup_view(self):
        response = self.client.post(reverse('profile:register'), {'username': 'newuser', 'email': 'newuser@example.com', 'password1': 'newpassword12', 'password2': 'newpassword12'})
        self.assertEqual(response.status_code, 302)  # Redirected after successful signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_reset_password_request_view(self):
        response = self.client.post(reverse('profile:reset-password-request'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)  # Successful request for password reset

    def test_reset_password_validate_token_view(self):
        # Create a reset password token for the user
        token = ResetPasswordToken.objects.create(user=self.user)
        # Make a POST request to validate the token
        response = self.client.post(reverse('profile:reset-password-validate'), {'token': token.key})
        self.assertEqual(response.status_code, 200)  # Token validation successful

    def test_reset_password_confirm_view(self):
        # Create a reset password token for the user
        token = ResetPasswordToken.objects.create(user=self.user)
        # Make a POST request to confirm password reset
        response = self.client.post(reverse('profile:reset-password-confirm'), {'token': token.key, 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)  # Password reset successful

    def test_views_redirect_when_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile:login'))
        self.assertRedirects(response, reverse('profile:home'))  # Redirect to home if already authenticated

class TestPasswordTokenModel(TestCase):
    def test_token_expiry(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        token = ResetPasswordToken.objects.create(user=user)
        token.created_at = timezone.now() - timedelta(days=2)  # Expired token
        token.save()
        self.assertTrue(token.is_expired())  # Token should be expired

    def test_token_not_expired(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        token = ResetPasswordToken.objects.create(user=user)
        token.created_at = timezone.now() - timedelta(hours=23)  # Valid token
        token.save()
        self.assertFalse(token.is_expired())  # Token should not be expired
