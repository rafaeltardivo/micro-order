from rest_framework.exceptions import MethodNotAllowed
from rest_framework.viewsets import ModelViewSet

from .models import Shipping
from .serializers import ShippingSerializer


class ShippingViewSet(ModelViewSet):
    """ModelViewSet definition for Shipping."""
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

    def post(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
