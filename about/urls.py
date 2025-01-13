from django.urls import path
from about.views import AboutView

urlpatterns = [
    path('sobre/', AboutView.as_view(), name='about'),
]
