from rest_framework import viewsets, permissions
from store.models import Category, Product, ProductTag
from .serializers import CategorySerializer, ProductSerializer, ProductTagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ProductTagViewSet(viewsets.ModelViewSet):
    queryset = ProductTag.objects.filter(is_active=True)


