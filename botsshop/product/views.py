from django.shortcuts import render
from product.serializers import ProductSerializer
from django.db.utils import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product


class ProductListCreateView(APIView):
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

    def post(self, request, format=None):
        """
        This method will handle POST requests for adding a new 
        product to the shop's inventory.
        returns:
        201: Serialized response of the created product.
        400: For invalid POST request.
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            except IntegrityError as e:
                error_msg = {"Unique Constraint Violation": e.args}
                return Response(error_msg, status=status.HTTP_409_CONFLICT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)