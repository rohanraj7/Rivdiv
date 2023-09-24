from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Invoice

class InvoiceAPITest(APITestCase):
    def test_create_invoice(self):
        url = reverse('invoice-list')
        data = {
            "date": "2023-10-08",
            "customer_name": "A luna",
            "details": [
                {
                    "description": "Test Player",
                    "Quantity": 2,
                    "unit_price": "10.00",
                    "price": "20.00"
                }
            ]
        }
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        