from django.shortcuts import render, redirect
from .models import HomeSlider, HomeSlider2
from django.contrib.auth import authenticate, login as admin_login

# Create your views here.
def home(request):
    homeslider1 = HomeSlider.objects.all()
    homeslider2 = HomeSlider2.objects.all()
    return render(request, 'core/index.html', locals())

def homeslider(request):
    homslider2 = HomeSlider2.objects.all()
    return render(request, 'core/homeslider.html', locals())

def blog(request):
    return render(request, 'core/blog.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

# Login View.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            admin_login(request, user)
            # messages.success(request, 'successfully logged in')
            return redirect('/dashboard/')
        else:
            # messages.error(request, 'something went wrong')
            return redirect('/login/')
    return render(request, 'core/login.html')
