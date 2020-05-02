from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Shipping

class ShippingSerializer(serializers.ModelSerializer):
    """Serializer definition for Shipping."""

    class Meta:
        model = Shipping
        fields = ('__all__')
