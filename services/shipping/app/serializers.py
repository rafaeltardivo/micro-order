from rest_framework import serializers

from .models import Shipping


class ShippingSerializer(serializers.ModelSerializer):
    """Serializer definition for Shipping."""
    status = serializers.CharField(source="get_status_display", read_only=True)
    shipped_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Shipping
        fields = ('__all__')
