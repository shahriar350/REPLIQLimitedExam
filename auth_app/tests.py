from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User


class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create_company(phone_number="01752495467",password="123456",name="Saifullah shahen")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
