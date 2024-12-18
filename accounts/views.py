from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
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
        
        # Validação
        if email and password:            
            if len(password) != 8:
                return HttpResponseRedirect(reverse_lazy('login'))
        
        # Capturando o usuário com o email
        user_object = User.objects.get(email=email)
        
        # Verificando as credenciais
        user = authenticate(self.request, username=user_object.username, password=password)

        # Se as credenciais estiverem corretas, autentique o usuário
        if user and email == user_object.email:
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy('login'))
        
        return HttpResponseRedirect(reverse_lazy('login'))
    

class RegisterView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'register.html')

    def post(self, *args, **kwargs):
        pass
