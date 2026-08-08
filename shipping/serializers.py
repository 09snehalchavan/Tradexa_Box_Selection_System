from rest_framework import serializers
from .models import Box, Product, Order


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    recommended_box = BoxSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'