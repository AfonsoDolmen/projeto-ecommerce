from django.views.generic import ListView, DetailView
from products.models import Product

class ProductsListView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'products.html'
    paginate_by = 10


class ProductDetailView(DetailView):
    pass
