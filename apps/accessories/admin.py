from django.contrib import admin

from apps.accessories.models import Accessory


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['restock_date']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 100
