from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class ChargeFelow(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.token_url = reverse('token_obtain_pair')
        self.admin_token = self.login("admin", "admin")
        self.seller_token = self.login("amirhosein", "1234")

    def login(self, username, password):
        data = {
            'username': username,
            'pasword': password,
        }
        response = self.client.post(url='http://localhost:8000/api/token/', data=data, format='json')
        print(response)
        print(response.data['access'])
        return response.data['access']
    




    def test_charge_client(self):
        headers = {
            "Authorization":f'Bearer {self.seller_token}'
        }
        data = {
            'phone_number': '+989120853818',
            'amount': 20000,
        }
        response = self.client.post(url='http://localhost:8000/api/token/',headers=headers, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data['field1'], 'value1')