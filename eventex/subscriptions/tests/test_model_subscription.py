from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Lidiane Monteiro',
            cpf='121313515',
            email='contato.lidymonteiro@gmail.com',
            phone='32-21313515'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription must have an auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)