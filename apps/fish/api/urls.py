from rest_framework.routers import DefaultRouter

from apps.fish.api.views import FishViewSet


router = DefaultRouter()

router.register('fish', FishViewSet)

urlpatterns = router.urls
