from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
):
    """Create/List/Detail view for Customers."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
