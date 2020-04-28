from django.urls import path

from .views import ShippingCreateView

urlpatterns = [
    path('', ShippingCreateView.as_view(), name='shipping_create')
]