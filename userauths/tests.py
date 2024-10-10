# test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient
from userauths.models import User

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userauths.views import RegisterView, LoginView, LogoutView


class LoginViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
            username="testuser",
        )

    def test_login_valid_user(self):
        response = self.client.post(reverse('userauths:sign-in'), {
            'email': 'test@example.com',
            'password': 'password123',
        })
        self.assertRedirects(response, reverse('book:book'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_login_invalid_user(self):
        response = self.client.post(reverse('userauths:sign-in'), {
            'email': 'wrong@example.com',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_login_with_empty_credentials(self):
        response = self.client.post(reverse('userauths:sign-in'), {
            'email': '',
            'password': '',
        })
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')



# test_apis.py
class UserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
            username="testuser",
        )

    def test_user_api_get(self):
        response = self.client.get(f'/user/api/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

    def test_user_api_post(self):
        new_user_data = {
            'email': 'new@example.com',
            'password': 'password123',
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
        }
        response = self.client.post('/user/api/create/', new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_api_patch(self):
        patch_data = {'first_name': 'Updated'}
        response = self.client.patch(f'/user/api/{self.user.id}/', patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Updated')
        
        
        
# test_urls.py
class TestUrls(SimpleTestCase):

    def test_register_url(self):
        url = reverse('userauths:sign-up')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_login_url(self):
        url = reverse('userauths:sign-in')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_url(self):
        url = reverse('userauths:sign-out')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

