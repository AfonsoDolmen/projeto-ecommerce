from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from contact.forms import ContactForm


class ContactView(View):
    def get(self, *args, **kwargs):
        form = ContactForm(data={'email': self.request.user.email})
        
        return render(self.request, 'contact.html', {
            'form': form,
        })

    def post(self, *args, **kwargs):
        form = ContactForm(data=self.request.POST)

        if form.is_valid() is True:
            form.save()

            return redirect(reverse_lazy('contact'))
        
        return render(self.request, 'contact')
