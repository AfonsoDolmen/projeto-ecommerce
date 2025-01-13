from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


class LoginView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')
    
    def post(self, *args, **kwargs):    
        # Coletando informações do formulário
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        
        # Validação
        if email and password:
            if "@" not in email or "." not in email:
                messages.error(self.request, 'Email inválido!')
                return HttpResponseRedirect(reverse_lazy('login'))

            if len(password) < 8:
                messages.error(self.request, 'A senha deve conter 8 ou mais caracteres.')
                return HttpResponseRedirect(reverse_lazy('login'))
        
        # Capturando o usuário com o email
        user_object = User.objects.get(email=email)
        
        # Verificando as credenciais
        user = authenticate(self.request, username=user_object.username, password=password, email=email)

        # Se as credenciais estiverem corretas, autentique o usuário
        if user:
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
        
        messages.error(self.request, 'Login inválido!')
        return HttpResponseRedirect(reverse_lazy('login'))
    

class RegisterView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'register.html')

    def post(self, *args, **kwargs):
        # Coletando informações do formulário
        username = self.request.POST.get('username')
        email = self.request.POST.get('email')
        password = self.request.POST.get('password')
        confirm_password = self.request.POST.get('confirm-password')

        # Validações
        if "@" not in email or "." not in email:
            messages.error(self.request, 'Email inválido!')
            return HttpResponseRedirect(reverse_lazy('register'))
        
        if len(password) < 8:
            messages.error(self.request, 'Senha deve conter 8 ou mais caracteres!')
            return HttpResponseRedirect(reverse_lazy('register'))

        if password != confirm_password:
            messages.error(self.request, 'As senhas não são iguais!')
            return HttpResponseRedirect(reverse_lazy('register'))
        
        
        # Verifica se já existe um usuário cadastrado
        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'Já existe um usuário com este nome!')
            return HttpResponseRedirect(reverse_lazy('login'))
        
        if User.objects.filter(email=email).exists():
            messages.error(self.request, 'Já existe um usuário com este email!')
            return HttpResponseRedirect(reverse_lazy('login'))
        
        # Se tudo estiver certo, crie um novo usuário
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        messages.success(self.request, 'Usuário cadastrado com sucesso! Por favor, faça login.')
        return HttpResponseRedirect(reverse_lazy('home'))
    

class LogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        
        return HttpResponseRedirect(reverse_lazy('home'))
