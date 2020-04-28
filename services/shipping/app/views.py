from rest_framework.generics import CreateAPIView

from .serializers import ShippingSerializer
from .models import Shipping

class ShippingCreateView(CreateAPIView):
    """CreateView definition for Shipping."""
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
