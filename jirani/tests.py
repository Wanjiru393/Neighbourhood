from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Kiambu = neighbourhood(neighbourhood='Kiambu')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kiambu,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Kiambu.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Kiambu.delete_neighbourhood('Kiambu')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.Screening = healthservices(healthservices='Screening')

    def test_instance(self):
        self.assertTrue(isinstance(self.Screening,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Screening.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Screening.delete_healthservices('Screening')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)