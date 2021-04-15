from django.shortcuts import render

def get_home(request):
    template = 'index.html'
    return render(request, template)

# Create your views here.
