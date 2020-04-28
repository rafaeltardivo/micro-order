from rest_framework.exceptions import MethodNotAllowed
from rest_framework.viewsets import ModelViewSet

from . import logger
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    """ModelViewSet definition for Order."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        logger.info("CREATE request: {}".format(request.data))
        return super().post(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
