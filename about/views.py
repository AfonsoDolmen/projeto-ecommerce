from django.shortcuts import render
from django.views import View


class AboutView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'about.html')
