from rest_framework import serializers

from .models import Shipping


class ShippingSerializer(serializers.ModelSerializer):
    """Serializer definition for Shipping."""
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = Shipping
        fields = ('__all__')
