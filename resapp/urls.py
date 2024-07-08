from django.urls import path,include
from . import views
import services

urlpatterns = [
    path('', views.home, name ='home'),
    path('services',include('services.urls')),
    path('contacts',views.contacts,name ='contacts'),
]
