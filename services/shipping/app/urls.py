from rest_framework import routers

from .views import ShippingViewSet

router = routers.SimpleRouter()
router.register("", ShippingViewSet, base_name="shippings")
urlpatterns = router.urls
