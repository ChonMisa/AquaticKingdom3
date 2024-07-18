from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from core.swagger import docs

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('', include('apps.fish.urls')),
    path('', include('apps.fish_food.urls')),
    path('', include('apps.accessories.urls')),
    path('', include('apps.cart.urls')),
    path('', include('apps.users.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
] + [
    path('api/', include('apps.fish.api.urls')),
    path('api/', include('apps.accessories.api.urls')),
    path('api/', include('apps.fish_food.api.urls')),
    path('api/', include('apps.categories.api.urls')),
    path('api/', include('apps.cart.api.urls')),
    path('api/', include('apps.users.api.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', docs.with_ui('swagger', cache_timeout=0), name="docs"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
