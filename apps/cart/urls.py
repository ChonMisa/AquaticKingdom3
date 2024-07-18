from django.urls import path

from apps.cart.views import CartDetailView, QuantityChangeLogics, QuantityChangeLogics2


urlpatterns = [
    path('cart/', CartDetailView.as_view(), name="cart"),
    path('minus/<int:pk>', QuantityChangeLogics.minus_quantity, name="minus_quantity"),
    path('plus/<int:pk>', QuantityChangeLogics2.plus_quantity, name="plus_quantity"),
]
