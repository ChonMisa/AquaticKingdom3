from rest_framework.routers import DefaultRouter
from apps.fish_food.api.views import FishFoodViewSet

router = DefaultRouter()

router.register('fish-food', FishFoodViewSet)

urlpatterns = router.urls
