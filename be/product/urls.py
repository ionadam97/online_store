from django.urls import path
from .views import (
    ProductsListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryAPIView,
    CreateProductView,
    SearchListAPIView,
)


urlpatterns = [
    path("product/", ProductsListAPIView.as_view(), name="products"),
    path("product/<int:pk>/", ProductDetailAPIView.as_view(), name="product_detail"),
    path("product/create/", CreateProductView.as_view(), name="create_product"),

    path("category/", CategoryListAPIView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryAPIView.as_view(), name="category_detail"),
    path("search/", SearchListAPIView.as_view(), name="search"),
]
