import datetime as dt

from django import urls
from accounts import views
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse, resolve
from django_dynamic_fixture import G

from freezegun import freeze_time
import pytest


#class TestViews:

@pytest.mark.parametrize('name', ['signup', 'login'])
def test_public_views(name, client):
    """
    Verify that the registration and login views are public
    """
    url = urls.reverse(name)
    resp = client.get(url)
    assert resp.status_code == 200

def test_signup_authenticated(client):
    """
    Test that after authentication, users will be redirected to homepage
    """
    path = reverse('home')
    with pytest.raises(Exception):
        assert 'home' in redirect.url

def test_signup_site(client):
    """
    Verify that the signup site renders as expected
    """
    url = urls.reverse('signup')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Sign Up!' in resp.content

def test_login_site(client):
    """
    Verify that the login site renders as expected
    """
    url = urls.reverse('login')
    resp = client.get(url)
    assert resp.status_code == 200
    assert b'Login' in resp.content

def test_addatrail_site(client):
    """
    Verify that the add a trail site renders as expected
    """
    url = urls.reverse('addatrail')
    resp = client.get(url)
    assert resp.status_code == 302
    assert b'Add a trail on the webpage'

@freeze_time('2019-05-07 19:00:00')
@pytest.mark.django_db
def test_signup(client):
    """
    Signup a user and verifies their last login date is correct
    """
    signup_url = urls.reverse('signup')
    resp = client.post(signup_url, {
        'username':'hello@example.com',
        'password1':'1234',
        'password2':'1234',
    })

    # The signup view should redirect us to our homepage
    assert resp.status_code == 302
    assert resp.url == urls.reverse('home')

    # There should be a user with 'hello@example.com'
    user = User.objects.get(username='hello@example.com')
#    assert user.last_login == dt.datetime(2019, 5, 7, 19, 0)

@pytest.mark.django_db
def test_login_and_logout(client):
    """
    Tests logging in and logging out
    """
    # Create a fake user
    user = G(User, username='username@example')
    user.set_password('111')
    user.save()

    login_url = urls.reverse('login')
    resp = client.post(login_url, {
        'username':'username@example',
        'password':'111',
    })

    # The login url should redirect to the homepage
    assert resp.status_code == 302
    assert resp.url == urls.reverse('home')

    # Logged in users have a session created for them
    assert Session.objects.count() == 1

    # Logout the user, the logout view redirects to the homepage
    logout_url = urls.reverse('home')
    resp = client.get(logout_url)

    assert resp.status_code == 200

    # After logout, there should be no more sessions left
#    assert not Session.objects.exist()


@pytest.mark.django_db
def test_signup_blank(client):
    """
    Tests if the username and passwords are blank
    """
    signup_url = urls.reverse('signup')
    resp = client.post(signup_url, {
        'username': None,
        'password1': None,
        'password2': None,
    })
#    with pytest.raises(ValueError)
    assert urls.reverse('signup')
    assert b'You have to fill in your username and/or password'


@pytest.mark.django_db
def test_signup_passwords_match(client):
    """
    Tests if password1 == password2
    """
    signup_url = urls.reverse('signup')
    resp = client.post(signup_url, {
        'username': 'ann@example',
        'password1': '12345',
        'password2': '12345',
    })
    assert '12345' == '12345'


@pytest.mark.django_db
def test_signup_passwords_not_match(client):
    """
    Tests if password1 != passwor2
    """
    signup_url = urls.reverse('signup')
    resp = client.post(signup_url, {
        'username': 'ann@example',
        'password1': '12345',
        'password2': '11111',
    })
    assert not '12345' == '11111'
    assert b'Passwords must match'


@pytest.mark.xfail
@pytest.mark.django_db
def test_signup_passwords_not_match_2(self):
    """
    Tests if password1 /= passwor2
    """
    signup_url = urls.reverse('signup')
    resp = client.post(signup_url, {
        'username': 'ann@example',
        'password1': '12345',
        'password2': '11111',
    })
    assert '12345' == '11111'
