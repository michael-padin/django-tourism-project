from django.shortcuts import render

# Create your views here.


# HOME PAGE
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')

def beaches(request):
    return render(request, 'beaches.html')


def hotels(request):
    return render(request, 'hotels.html')
