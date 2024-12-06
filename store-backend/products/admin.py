from django.contrib import admin
from .models import Product, ProductImage

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "description", "available"]  # 'available' added
    list_filter = ["available"]  # Add filter for availability
    search_fields = ["title", "description"]
    inlines = [ProductImageInline]