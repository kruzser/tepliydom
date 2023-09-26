from rest_framework import serializers

from .models import Category, Product, Filters


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "price",
            "get_image",
            "get_thumbnail",
            "brand"
        )


class CategorySerializer(serializers.ModelSerializer):
    products = []
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )

class FilterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "slug"
        )
