from django import forms
from products.models import Product


class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
            ]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do produto',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descreva o produto',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o preço do produto',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a quantidade em estoque',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a url (ex: blusa-de-inverno)',
            }),
        }

    def clean_price(self):
        price = self.cleaned_data['price']

        if price is 0:
            self.add_error('price', 'O preço não pode ser 0.')

        if price < 50:
            self.add_error('price', 'O preço não pode ser menor que 50.')

        return price

    def clean_stock(self):
        stock = self.cleaned_data['stock']

        if stock is 0:
            self.add_error('stock', 'A quantidade não pode ser 0.')

        return stock
