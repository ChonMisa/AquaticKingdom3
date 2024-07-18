from django.contrib import admin

from apps.fish_food.models import FishFood


@admin.register(FishFood)
class FishFoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title', 'restock_date']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
