from django.shortcuts import render

# Create your views here.

def servView(request):
    return render(request, 'services.html')
