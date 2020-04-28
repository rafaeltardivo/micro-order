from rest_framework.generics import CreateAPIView

from .serializers import CustomerSerializer
from .models import Customer

class CustomerCreateView(CreateAPIView):
    """CreateView definition for Customer."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
