from rest_framework import serializers
from .models import Product, Price, Type


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
