from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Shipping

class ShippingSerializer(serializers.ModelSerializer):
    """Serializer definition for Shipping."""

    class Meta:
        model = Shipping
        fields = ('__all__')
        read_only = ('id', 'shipped_at')

    def validate_order(self, value):
        """Order id validation."""

        if value < 0:
            raise ValidationError("Must be greater then 0.")
        return value
