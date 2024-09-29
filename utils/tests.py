from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class YourModelTests(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('charge-client')

    def test_create_object(self):
        data = {
            'field1': 'value1',
            'field2': 'value2',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['field1'], 'value1')