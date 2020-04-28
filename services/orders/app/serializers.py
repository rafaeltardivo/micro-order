from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """Serializer definition for Order."""

    class Meta:
        model = Order
        exclude = ("id", )

    def validate_customer(self, value):
        """Customer id validation."""

        if value < 0:
            raise ValidationError("Must be greater then 0.")
        return value



