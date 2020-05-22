from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serializer definition for Order."""
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only = ("id", "made_at")

    def validate_customer(self, value):
        """Customer id validation.
        Args:
            value (int): Customer id.
        Returns:
            value (int): Customer id.
        """

        if value < 0:
            raise ValidationError("Must be greater then 0.")
        return value
