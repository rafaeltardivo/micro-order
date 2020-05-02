from rest_framework.generics import ListAPIView

from .serializers import ShippingSerializer
from .models import Shipping

from . import logger

class ShippingListView(ListAPIView):
    """ListView definition for Shipping."""
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

    def list(self, request, *args, **kwargs):
        logger.info("Shipping list request")
        return super().list(request, *args, **kwargs)
