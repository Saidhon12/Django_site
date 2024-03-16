from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import Product
from.forms import *
# Create your views here.

def dashboard(request):
    Products = Product.objects.all()
    return render(request, 'dashboard.html', {'products':Products})

def register(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            return render('success')
        else:
            return render('error')
    else:
        form = userform()
    return render(request,'register.html')
   
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return render('success')
        else:
            return render('error')
    else:
        form = LoginForm()
    return render(request, 'login.html')

def log_admin(request):
    if request.method == 'POST':
        form = Admin(request.POST)
        if form.is_valid():
            form.save()
            return render('success')
        else:
            return render('error')
    else:
        form = Admin()
    return render(request, 'login_admin.html')

@login_required(login_url='login')
def addadmin(request):
    if request.method == 'POST':
        form = Admin(request.POST)
        if form.is_valid():
            form.save()
            return render('success')
        else:
            return render('error')
    else:
        form = Admin()
    return render(request, 'addadmin.html')


