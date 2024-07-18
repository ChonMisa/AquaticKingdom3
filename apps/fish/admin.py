from django.contrib import admin
from apps.fish.models import Fish, FishImage


class FishImageInline(admin.TabularInline):
    model = FishImage
    extra = 1


@admin.register(FishImage)
class FishImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Fish)
class MainFishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['category', 'restock_date']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FishImageInline]
