from django.shortcuts import render
from django.views.generic import View


class LoginView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')
    
    def post(self, *args, **kwargs):
        pass
