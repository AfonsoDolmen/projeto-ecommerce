from django.urls import path
from accounts.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
]
