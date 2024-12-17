from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


class LoginView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')
    
    def post(self, *args, **kwargs):    
        # Coletando informações do formulário
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        
        user_object = User.objects.get(email=email)
        
        # Verificando as credenciais
        user = authenticate(self.request, username=user_object.username, password=password)

        if user and email == user_object.email:
            login(self.request, user)
            return HttpResponseRedirect('/login/')
        
        return HttpResponseRedirect('/login/')
