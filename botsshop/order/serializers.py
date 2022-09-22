from rest_framework import serializers

from order.models import Order
from product.models import Product
from client.models import Client


class OrderSerializer(serializers.ModelSerializer):
    """A model serializer class for the Order model."""
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=False)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = "__all__"

    def get_total_price(self, obj):
        return obj.total_price()