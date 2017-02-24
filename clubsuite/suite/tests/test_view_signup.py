from django.test import TestCase
from django.test import Client
from suite.views import RegistrationView
from django.urls import reverse

class RegistrationViewTestCase(TestCase):
    def setUp(self):

        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('suite:register'))
        self.assertEqual(response.status_code,200)

        #self.assertRedirects(response, reverse('suite:register'))
    
    def test_post(self):
        data={'first_name':"John",
                'last_name':"Doe",
                'email':"test@test.com",
                'password1':"clubsuite",
                'password2':"clubsuite"
                }
        response=self.client.post(reverse('suite:register'),data,follow=True)
        self.assertRedirects(response,reverse('suite:register_done'))

    def test_post_fail(self):
        data={'first_name':"John",
                'last_name':"Doe",
                'email':"test@test.com",
                'password1':"clubsuite"
                }
        response=self.client.post(reverse('suite:register'),data,follow=True)
        self.assertEqual(response.status_code,200)
    '''
    def test_get(self):
        response = self.client.get(reverse('suite:club_create'))
        #self.assertEqual(response.status_code,200)
        self.assertRedirects(response, reverse('suite:club_create'), 302,200)

    def test_post(self):
        data = {
                'club_name':"Club",
                'club_type':"PUB",
                'club_description':"Pretty cool"
                }
        response = self.client.post(reverse('suite:club_create'),data, follow=True)
        self.assertEqual(response.status_code,200)

    #    def test_post_invalid(self):
    '''

