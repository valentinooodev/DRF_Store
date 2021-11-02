from rest_framework import serializers
from store.models import Category, Product, ProductImage, ProductTag


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'slug')
        model = Category


class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name',)
        model = ProductTag


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tags = ProductTagSerializer(many=True)
    image_url = serializers.CharField(source='get_absolute_image_url')

    class Meta:
        fields = ('category', 'id', 'name', 'slug', 'description', 'content', 'image_url', 'price', 'tags', 'is_active')
        model = Product
