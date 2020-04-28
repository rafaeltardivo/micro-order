from django.urls import path

from .views import CustomerCreateView

urlpatterns = [
    path('', CustomerCreateView.as_view(), name='customer_create')
]