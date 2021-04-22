from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ProductType, Fabric

def index(request):
    return redirect('/home')

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

@login_required(login_url='/login/')
def get_contact(request):
    template = 'contact.html'
    return render(request, template)

@login_required(login_url='/login/')
def get_product(request):
    product = ProductType.objects.all()
    template = 'product.html'
    return render(request, template, {'product': product})

def get_visit(request):
    template = 'fabric.html'
    fabrics = Fabric.objects.all()
    return render(request, template, {'fabric':fabrics})

# Create your views here.
