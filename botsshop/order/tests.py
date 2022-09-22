import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from order.models import Client
from product.models import Product

from product.tests import DEMO_PRODUCT
from client.tests import DEMO_CLIENT


DEMO_CLIENT_ORDER = {
    "client": 1,
    "product": 1,
    "quantity": 1,
    "placed_on": "2022-08-30T14:42:45.614956+01:00"
}


# API tests
class ClientOrderHistoryViewTestCase(APITestCase):
    """
    This test suite will test the api end point that
    displays the history of orders made by a client in the shop.
    """
    order_history_url = reverse('order:history')
    def setUp(self):
        """
        The setUp method that will run before every test case defined.
        """
        demo_product = Product.objects.create(**DEMO_PRODUCT)
        demo_client = Client.objects.create(**DEMO_CLIENT)

        self.client.force_login(demo_client)
        self.response = self.client.post(self.order_history_url, DEMO_CLIENT_ORDER, format='json')
    
    def test_client_order_creation(self):
        """
        Testing the api point feature for creating a new client order.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_client_order_get_method(self):
        """
        Testing the api point feature for listing all orders that have 
        been made by a particular client.
        """
        get_response = self.client.get(self.order_history_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertDictContainsSubset(DEMO_CLIENT_ORDER, json.loads(get_response.content)[0])