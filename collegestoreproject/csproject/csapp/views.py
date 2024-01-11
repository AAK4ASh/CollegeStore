from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import  auth
# Create your views here.
def index(request):
    return render(request,'index.html')
def form(request):
    return render(request,'form.html')
def message(request):
    return render(request,'message.html')
def login(request):
    if request.method=="POST":
        usernamel=request.POST['username_l']
        passwordl=request.POST['password_l']
        userdb=auth.authenticate(username=usernamel,password=passwordl)
        if userdb is not None:
            auth.login(request,userdb)
            return redirect('form')
        else:
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username_r']
        password=request.POST['password_r']
        cpassword=request.POST['cpassword_r']
        if password==cpassword:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('login')
        else:
            return redirect('/')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('index')