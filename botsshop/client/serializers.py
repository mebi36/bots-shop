from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        """
        Overriding the default create method of the serializer
        to set/hash clien password.
        """
        if "password" in validated_data:
            password = validated_data.pop("password")
            client = super().create(validated_data)
            client.set_password(password)
            client.save()
            return client
        return super().create(validated_data)
