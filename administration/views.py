from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    pass


class ProductCreateView(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    pass


class ProductUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    pass


class ProductDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    pass
