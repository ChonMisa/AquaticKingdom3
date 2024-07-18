from django.urls import path

from apps.fish_food.views import FFoodListView, FFoodDetailView

urlpatterns = [
    path('ffoods/', FFoodListView.as_view(), name='ffood_list'),
    path('ffoods/<slug:slug>/', FFoodDetailView.as_view(), name='ffood_detail')
]
