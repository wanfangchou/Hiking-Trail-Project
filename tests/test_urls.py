import pytest

from django.urls import reverse, resolve

class TestUrls:

    def test_home_url(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_signup_url(self):
        path = reverse('signup')
        assert resolve(path).view_name == 'signup'

    def test_login_url(self):
        path = reverse('login')
        assert resolve(path).view_name == 'login'

    def test_logout_url(self):
        path = reverse('logout')
        assert resolve(path).view_name == 'logout'

    def test_addatrail_url(self):
        path = reverse('addatrail')
        assert resolve(path).view_name == 'addatrail'
