from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def home(request):
    return render(request, 'homepage/Homepageback.html')

def catalog(request):
    return render(request, 'homepage/catalog.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)
            return redirect('homepage:home')
    else:
        form = SignUpForm()
    return render(request, 'homepage/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage:home')
    else:
        form = SignInForm()
    return render(request, 'homepage/signin.html', {'form': form})

def cart(request):
    return render(request, 'homepage/Shopping Cart.html')

def productdetails(request):
    return render(request, 'homepage/Productpage.html')

def checkout1(request):
    return render(request, 'homepage/CheckIn1.html')

def checkout2(request):
    return render(request, 'homepage/CheckIn2.html')

def checkout3(request):
    return render(request, 'homepage/CheckIn3.html')