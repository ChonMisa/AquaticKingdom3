from rest_framework.routers import DefaultRouter

from apps.cart.api.views import CartViewSet, OrderViewSet

router = DefaultRouter()

router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls
