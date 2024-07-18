from django.views import generic
from django.shortcuts import redirect

from apps.cart.models import Cart, Item


class CartDetailView(generic.ListView):
    template_name = '/'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class QuantityChangeLogics:
    @staticmethod
    def minus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return redirect('cart')

        item.quantity -= 1
        item.save()
        return redirect('cart')


class QuantityChangeLogics2:
    @staticmethod
    def plus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart')
