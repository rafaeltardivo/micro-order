from rest_framework.generics import CreateAPIView

from .serializers import OrderSerializer
from .models import Order

from . import logger

class OrderCreateView(CreateAPIView):
    """CreateView definition for Order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        logger.info("Order create request", extra={'payload': request.data})
        return super().post(request, *args, **kwargs)
