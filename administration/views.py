from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from products.models import Product
from administration.forms import CreateProductForm


class ProductListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Product
    context_object_name = 'products'
    template_name = 'admin_list.html'
    paginate_by = 10


class ProductCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Product
    template_name = 'admin_create.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('admin_list')


class ProductUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    pass


class ProductDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    pass
