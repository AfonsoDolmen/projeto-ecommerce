from django.urls import path
from contact.views import ContactView

urlpatterns = [
    path('contato/', ContactView.as_view(), name='contact'),
]

