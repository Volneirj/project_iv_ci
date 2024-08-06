from django.test import TestCase
from django.urls import reverse

class AboutPageTest(TestCase):

    def test_about_page_status_code(self):
        """
        Test that the About page returns a 200 status code.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        """
        Test that the About page uses the correct template.
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_page_content(self):
        """
        Test that the About page contains the correct content.
        """
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'About')
        self.assertContains(response, 'About Our Library System')
