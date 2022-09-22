from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from order.serializers import OrderSerializer
from order.models import Order


class ClientOrderHistoryView(APIView):
    """
    The API view for client orders.
    
    urlpattern:
        api/v1/order/history/

    Accepts:
        'GET' (returns list of all orders the client making the request 
        has ever placed.)
        'post' (adds a new order by the client to the order history)
    
    Client must be logged in to view/add to order history.
    permission_class: rest_framework.permissions.IsAuthenticated
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        This method handles retrieving all orders that were made by
        a given client.
        """
        orders = Order.objects.filter(client=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        This method handles the creation of a new
        order for a particular client in the system.
        """
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                error_msg = {"Unique Constraint Violation": e.args}
                return Response(error_msg, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
