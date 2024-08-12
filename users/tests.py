from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupViewTests(TestCase):
    """
    Test suite for the user signup view.
    """
    def setUp(self):
        """
        Set up the test client and URL for the signup view.
        """
        self.client = Client()
        self.signup_url = reverse('signup')

    def test_signup_form_renders_correctly(self):
        """
        Test that the signup page renders correctly.

        Verifies that the signup page returns a 200 status code,
        uses the correct template, and includes a UserCreationForm
        in the context.
        """
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')
        self.assertIsInstance(
            response.context['form'],
            UserCreationForm)

    def test_signup_successful(self):
        """
        Test that a user can sign up successfully.

        Posts valid user data to the signup view,
        verifies the response is a redirect
        to the home page, and confirms that the user
        has been created and can log in.
        """
        data = {
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(
            username='testuser').exists())
        user = User.objects.get(username='testuser')
        self.assertTrue(self.client.login(
            username='testuser', password='securepassword123'))

    def test_signup_form_invalid(self):
        """
        Test that the signup form fails with invalid data.

        Posts data with mismatched passwords to the signup
        view and verifies that the form returns
        an error message and that no user is created.
        """
        data = {
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'differentpassword123'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)

        expected_error_message = 'The two password fields didn’t match.'
        self.assertFormError(response,
                             'form',
                             'password2', expected_error_message)
        self.assertFalse(
            User.objects.filter(username='testuser').exists())

    def test_signup_no_data(self):
        """
        Test that the signup form returns errors when
        no data is submitted.

        Submits an empty form and verifies that
        the form returns required field errors
        for the username, password1, and password2 fields.
        """
        response = self.client.post(self.signup_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response,
                             'form', 'username', 'This field is required.')
        self.assertFormError(response,
                             'form', 'password1', 'This field is required.')
        self.assertFormError(response,
                             'form', 'password2', 'This field is required.')
