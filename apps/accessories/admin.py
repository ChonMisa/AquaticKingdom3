from django.contrib import admin

from apps.accessories.models import Accessory, AccessoryImage


class AccessoryImageInline(admin.TabularInline):
    model = AccessoryImage
    extra = 1


@admin.register(AccessoryImage)
class AccessoryImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['restock_date']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 100
    inlines = [AccessoryImageInline]
