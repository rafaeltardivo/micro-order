from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer definition for Customer."""

    class Meta:
        model = Customer
        fields = '__all__'
        read_only = ("id", "made_at")


