from django.test import TestCase, Client
from accounts.views import *

c = Client()
response = c.post('/login/', {'username':'BOY', 'password': '123'})
response.status_code
