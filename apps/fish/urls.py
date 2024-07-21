from django.urls import path

from apps.fish.views import FishListView, FishDetailView

urlpatterns = [
    path('', FishListView.as_view(), name="fish_list"),
    path('fish/<str:slug>', FishDetailView.as_view(), name="fish_detail"),
]
