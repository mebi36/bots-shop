from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import OrderSerializer
from .models import Order


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