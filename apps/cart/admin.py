from django.contrib import admin
from apps.cart.models import Cart, Item, Order
from apps.fish_food.models import FishFood
from apps.fish.models import Fish
from apps.accessories.models import Accessory

# admin.site.register(Cart)
# admin.site.register(Item)
# admin.site.register(Order)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_total_sum')
    search_fields = ('user__username', )
    readonly_fields = ('get_total_sum', )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('fish', 'accessory', 'ffood', 'quantity', 'cart', 'get_subtotal_sum')
    search_fields = ('fish__name', 'accessory__title', 'ffood__title', 'cart__user__username')
    readonly_fields = ('get_subtotal_sum',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at', 'status', 'delivery_type')
    list_filter = ('status', 'delivery_type', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at', 'updated_at')

#
# @admin.register(Fish)
# class FishAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock', 'restock_date')
#     search_fields = ('name')
#     list_filter = ('restock_date')
#
#
# @admin.register(Accessory)
# class AccessoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'stock', 'restock_date')
#     search_fields = ('title')
#     list_filter = ('restock_date',)
#
#
# @admin.register(FishFood)
# class FishFoodAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'stock', 'restock_date')
#     search_fields = ('title')
#     list_filter = ('restock_date',)
