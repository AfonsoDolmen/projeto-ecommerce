from django.urls import path
from administration.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('administration/', ProductListView.as_view(), name='admin_list'),
    path('administration/create/', ProductCreateView.as_view(), name='admin_create'),
    path('administration/<slug:slug>/', ProductUpdateView.as_view(), name='admin_update'),
    path('administration/<slug:slug>/delete/', ProductDeleteView.as_view(), name='admin_delete'),
]
