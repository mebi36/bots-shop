from django.shortcuts import render
from product.serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product


class ProductListView(APIView):
    """The API view for products offered by the shop."""
    def get(self, request, format=None):
        """
        This method will handle GET requests for retrieving all
        the products offered by the shop.
        returns:
        200: Serialized response of the list of products. will return
        an empty json array if no products are offered by the shop. 
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)