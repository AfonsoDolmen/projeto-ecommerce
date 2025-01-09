from django.form import ModelForm
from django.core.excepetions import ValidationError
from products.models import Product


class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
            ]
