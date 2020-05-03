from rest_framework import routers

from .views import OrderViewSet

router = routers.SimpleRouter()
router.register("", OrderViewSet, base_name="orders")
urlpatterns = router.urls
