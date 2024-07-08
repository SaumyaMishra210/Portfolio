from django.urls import path
from . import views

urlpatterns = [
    path('edu/',views.eduView, name = 'edu'),
]
