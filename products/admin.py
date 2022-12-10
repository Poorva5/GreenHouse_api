from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price', 'available']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}