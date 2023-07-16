# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, Client

class UserCreationTest(TestCase):
     def test_user_registration(self):
          # Create a new user
          username = 'testuser'
          password = 'testpassword'
          email = 'testuser@example.com'
          user = User.objects.create_user(username=username, password=password, email=email)

          # Verify user creation
          self.assertEqual(user.username, username)
          self.assertEqual(user.email, email)
          self.assertTrue(user.check_password(password))

class UserApiTest(TestCase):
     def setUp(self):
          self.client = Client()

     def test_get_data(self):
          # Make a GET request to the API endpoint
          response = self.client.get('/user/profile/1')

          # Assert the response status code
          self.assertEqual(response.status_code, 301)
