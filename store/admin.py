from django.contrib import admin

from .models import Category, Product, ProductImage, ProductTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'content', 'price', 'is_active', 'created', 'updated']
    list_filter = ['is_active']
    list_editable = ['price', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImage)
class ProDuctImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt', 'image']
    list_filter = ['is_main_image']


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']