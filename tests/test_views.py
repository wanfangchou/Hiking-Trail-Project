from accounts import views
from django.shortcuts import render, redirect
from django.urls import reverse, resolve

import pytest


class TestViews:

    def test_signup_authenticated(self):
        path = reverse('home')
        with pytest.raises(Exception):
            assert 'home' in redirect.url


#    def test_signup_blank():
#        """test if the username and passwords are blank"""
#        request.POST['username'] == None
#        request.POST['password1'] == None
#        request.POST['password2'] == None
#        with pytest.raises(ValueError):
#            assert test_signup_blank()

#    def test_signup_passwords_match():
#        """test if password1 == password2"""
#        if 'password1' == '123' and 'password2' == '123':
#            assert 'password1' == 'password2'

#    def test_signup_passwords_not_match(self):
#        """test if password1 /= passwor2"""
#        if 'password1' == '123' and 'password2' == '234':
#            assert "Passwords must match"

#    @pytest.mark.xfail
#    def test_signup_passwords_not_match_2(self):
#        """test if password1 /= passwor2"""
#        'password1' == 123 and 'password2' == 234
#        assert 'password1' == 'password2'
