from django.shortcuts import render, redirect
from .models import Contacts


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        if len(username) < 3 or len(username) > 50:
            error_message = "Username must be between 3 and 50 characters."
            return render(request, 'contacts.html', {'error_message': error_message})

        # Simple form validation
        if username and email and msg:
            user = Contacts(username=username, email=email, msg=msg)
            user.save()
            return redirect('home')
    return render(request, 'contacts.html')
