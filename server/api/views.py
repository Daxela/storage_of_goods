from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Product, Price, Type
from .serializers import ProductsSerializer, PricesSerializer, TypesSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class PriceListCreate(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PricesSerializer


class PriceRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PricesSerializer


class TypeListCreate(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer


class TypeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer


class ProductView(APIView):

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity_sold = request.data.get('quantity_sold')
        if not(product_id and quantity_sold):
            raise ValidationError
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound
        product.quantity -= int(quantity_sold)
        product.save()
        serializer = ProductsSerializer(product, many=False)
        return Response(serializer.data)
