from django.shortcuts import render
from django.views.generic import View
from products.models import Product


class HomeView(View):
    def get(self, *args, **kwargs):
        # Retorna somente os três ultimos produtos
        products = Product.objects.all().order_by('-id')[:3]
        
        return render(self.request, 'home.html', {'products': products})
