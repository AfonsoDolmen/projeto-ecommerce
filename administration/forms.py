from django.forms import ModelForm
from django.core.exceptions import ValidationError
from products.models import Product


class CreateProductForm(ModelForm):
    
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
            ]
