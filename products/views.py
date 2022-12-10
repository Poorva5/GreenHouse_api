from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import ProductSerialzier
from .models import Product
from rest_framework.permissions import AllowAny


class ProductList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier


class ProductDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    # lookup_field = id