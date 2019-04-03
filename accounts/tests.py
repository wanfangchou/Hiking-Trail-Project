from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from django.urls import path, include

from filters import views
from accounts import views

class SignUpPageTests(SimpleTestCase):

#    def test_signup_status_code(self):
#        response = self.client.get('/accounts/signup')
#        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

class LoginTests(SimpleTestCase):
    def test_view_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

class LogoutTests(SimpleTestCase):
    def test_view_url_by_name(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

if __name__ == '__main__':
    unittest.main()
