from django.urls import path
from products.views import ProductsListView, ProductDetailView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
