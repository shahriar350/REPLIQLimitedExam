from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User


class AnimalTestCase(TestCase):
    def text_create_user(self):
        user = User.objects.create_company(phone_number="01752495467", password="123456", name="Saifullah shahen")
        self.assertEqual(user)

