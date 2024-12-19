from django.views.generic import ListView, DetailView
from products.models import Product

class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.GET.get('category')

        # Filtragem pela categoria
        if category:
            queryset = Product.objects.filter(category__category=category.capitalize())

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
