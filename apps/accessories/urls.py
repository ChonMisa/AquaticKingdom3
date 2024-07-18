from django.urls import path

from apps.accessories.views import AccessoryListView, AccessoryDetailView

urlpatterns = [
    path('accessories/', AccessoryListView.as_view(), name='accessory_list'),
    path('accessories/<slug:slug>/', AccessoryDetailView.as_view(), name='accessory_detail')
]
