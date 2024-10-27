from django.contrib import admin
from .models import Collection, BestSeller, Shop

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'reviews_count')  # Use the correct field name
    search_fields = ('title', 'description')  # Enable search functionality

@admin.register(BestSeller)
class BestSellerAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

@admin.register(Shop)        
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'type', 'price')  # Fields to display
    search_fields = ('title', 'category', 'type')  # Searchable fields
    list_filter = ('category', 'type')  # Filters to use in the admin panel
