from django.shortcuts import render


# Create your views here.
def eduView(request):
    return render(request , 'skills.html')
