from rest_framework.routers import DefaultRouter
from .views import FCategoryViewSet

router = DefaultRouter()


router.register(r'categories', FCategoryViewSet)

urlpatterns = router.urls
