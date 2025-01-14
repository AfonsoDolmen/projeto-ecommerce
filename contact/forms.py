from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Assunto',
            }),
            
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Sua menssagem',
            }),
        }
