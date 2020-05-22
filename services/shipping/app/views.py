from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet

from .models import Shipping
from .serializers import ShippingSerializer


class ShippingViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
    """Create/List/Detail view for Shipping."""
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer