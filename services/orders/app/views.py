from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from .serializers import OrderSerializer
from .models import Order

class OrderCreateView(CreateAPIView):
    """CreateView definition for Order."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
