from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClientSerializer
from .models import Client


class ClientView(APIView):
    """ "The API view for the application's client model."""

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        This method handles retrieving objects of the Client model
        from the database.
        Returns:
        Client object if object with primary key pk is found.
        raises Http404 Error if the Client with primary key pk is not
        found.
        """
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        """
        This method handles a GET request for retrieving an
        existing client.
        Returns:
        200: A serialized response of the Client object for given
        primary key.
        404: Not found if the no client is found with primary key pk.
        """
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        """
        This method handles updating information for an existing
        client.
        Returns:
        200: A serialized response of the updated Client object for a
        given primary key.
        404: If no client is found with primary key pk
        400: A serialized response containing the details of offending fields
        the user provided for update.
        """
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ClientCreationView(APIView):
    """View handles creation of new Client objects"""

    def post(self, request, format=None):
        """
        This method handles creation of a new Client object with data
        provided to the endpoint.
        Returns:
        201: If object creation was successful
        400: A serialized response containing details of offending fields
        the user provided for the object creation.
        """
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
