from rest_framework.filters import SearchFilter
from .models import Product, Category
from .serializers import (
    ProductSerializer,
    ProductsSerializer,
    CategorySerializer,
    ProductCreateSerializer,
    CategoryProductsSerializer,
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


class ProductsListAPIView(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryListAPIView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(APIView):

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategoryProductsSerializer(category)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryProductsSerializer(category)
        return Response(serializer.data)


class SearchListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]


class CreateProductView(CreateAPIView):

    queryset = Product.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ProductCreateSerializer
