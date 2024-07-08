from django.urls import path,include
from . import views
import services

urlpatterns = [
    path('',views.index,name = 'index'),
    path('services',include('services.urls')),
    path('contacts',views.contacts,name ='contacts'),
]
