from rest_framework import serializers
from .models import Product, Category


class ProductSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'available', 'image', 'description', 'created', 'updated', 'planter_size', 'height']


class CategorySerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']
