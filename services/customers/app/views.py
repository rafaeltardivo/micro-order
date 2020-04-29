from rest_framework.generics import CreateAPIView

from .serializers import CustomerSerializer
from .models import Customer

from . import logger

class CustomerCreateView(CreateAPIView):
    """CreateView definition for Customer."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        logger.info("Customer create request", extra={'payload': request.data})
        return super().post(request, *args, **kwargs)
