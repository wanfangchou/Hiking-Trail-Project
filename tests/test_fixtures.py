import pytest

from django.db import connection, transaction
from django.db import settings as real_settings

from pytest_django.lazy_django import get_django_version
from pytest_django_test.app.models import Item
from pytest_django_test.compat import HTTPError, urlopen

def test_client(client):
    assert isinstance(client, Client)

@pytest.mark.django_db
def test_admin_client(admin_client):
    assert isinstance(admin_client, Client)
    resp = admin_client.get('/admin/')
    assert force_text(resp.content) == "You are an admin"
