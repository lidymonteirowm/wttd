from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Lidiane Monteiro', cpf='121313515',
                    email='contato.lidymonteiro@gmail.com', phone='32-21313515')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'lidiane.monteiro@fundaj.gov.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['lidiane.monteiro@fundaj.gov.br', 'contato.lidymonteiro@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Lidiane Monteiro',
            '121313515',
            'contato.lidymonteiro@gmail.com',
            '32-21313515',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)