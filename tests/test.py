import pytest

from django.conf import settings
from tinker import *


import pytest
def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code ==200
