from django.urls import path
from . import views

urlpatterns = [
    path('serv', views.servView, name = 'serv'),
]
