from rest_framework.routers import DefaultRouter
from .views import AccessoryViewSet

router = DefaultRouter()

router.register(r'accessories', AccessoryViewSet)

urlpatterns = router.urls
