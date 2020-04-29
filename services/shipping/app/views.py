from rest_framework.generics import CreateAPIView

from .serializers import ShippingSerializer
from .models import Shipping

from . import logger

class ShippingCreateView(CreateAPIView):
    """CreateView definition for Shipping."""
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

    def post(self, request, *args, **kwargs):
        logger.info("Shipping create request", extra={'payload': request.data})
        return super().post(request, *args, **kwargs)
