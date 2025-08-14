from django.urls import path, include
from . import views

urlpatterns = [
    # This line maps the homepage ('') to the 'home' view
    path('', views.home, name='home'),
]