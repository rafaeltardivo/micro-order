from rest_framework import routers

from .views import CustomerViewSet

router = routers.SimpleRouter()
router.register("", CustomerViewSet, base_name="shippings")
urlpatterns = router.urls
