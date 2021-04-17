from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return redirect('/login')

@login_required(login_url='/login/')
def get_home(request):
    template = 'index.html'
    return render(request, template)

def get_login(request):
    template = 'login.html'
    return render(request, template)

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/home')
        else:
            messages.error(request, 'Usuario ou senha inválido')
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

# Create your views here.
