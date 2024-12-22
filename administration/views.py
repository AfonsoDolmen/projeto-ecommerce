from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from products.models import Product


class ProductListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Product
    context_object_name = 'products'
    template_name = 'admin_list.html'
    paginate_by = 10


class ProductCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    pass


class ProductUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    pass


class ProductDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    pass
