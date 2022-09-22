from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from order.serializers import OrderSerializer
from order.models import Order


class ClientOrderHistoryView(APIView):
    """The API view for client orders."""
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
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
