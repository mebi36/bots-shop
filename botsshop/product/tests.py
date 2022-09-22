import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product

DEMO_PRODUCT = {
    "id": 1,
    "name": "Mars Rover - Table-top size",
    "description": "A table-top sized bot modeled after the Mars Rover 3",
    "price": '400000.00',
    "image": None,
    "available_qty": 25
}


# API tests
class ProductListCreateViewTestCase(APITestCase):
    """
    This Test case is for the api view ProductListCreateView.
    """
    def test_product_creation(self):
        """
        This is a test for the product creation feature of the api 
        point.
        """
        url = reverse('product:list-create')
        response = self.client.post(url, DEMO_PRODUCT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(DEMO_PRODUCT,json.loads(response.content))

    def test_product_list_view(self):
        """
        This is a test for the product listing feature of the api point
        """
        url = reverse('product:list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])

        # Testing the view with an existing product
        Product.objects.create(**DEMO_PRODUCT)
        response = self.client.get(url, format='json')
        self.assertDictContainsSubset(DEMO_PRODUCT, json.loads(response.content)[0])
    
    def test_duplicate_product_creation(self):
        """
        This is a test of the unique constraint that prevents duplication
        of exisiting products.
        """
        url = reverse('product:list-create')
        response = self.client.post(url, DEMO_PRODUCT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        duplicate_attempt_response = self.client.post(url, DEMO_PRODUCT, format='json')
        self.assertEqual(duplicate_attempt_response.status_code, status.HTTP_409_CONFLICT)