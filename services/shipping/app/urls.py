from django.urls import path

from .views import ShippingListView

urlpatterns = [
    path('', ShippingListView.as_view(), name='shipping_list')
]
