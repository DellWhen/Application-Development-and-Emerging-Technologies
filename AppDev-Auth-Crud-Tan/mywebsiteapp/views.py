from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.


def home(request):
    return render(request, 'home.html', {

    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Invalid username or password")
            return redirect('login')
    else:        
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  
        
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form=RegisterForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})