from rest_framework import serializers
from .models import Product, ProductImage  # Adjust the import path

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # For approach A

    class Meta:
        model = Product
        fields = "__all__"