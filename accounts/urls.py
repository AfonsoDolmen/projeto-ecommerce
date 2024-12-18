from django.urls import path
from accounts.views import LoginView, RegisterView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
