from django.shortcuts import render,redirect
from .models import Profile,Profile_pic
from database.models import User
from django.contrib import messages
import time
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="accounts/login")
def home(request):
    return render(request,"index.html")

@login_required(login_url="accounts/login")
def index(request):
    '''if request.session.get("status") == "logged in":
        img = User.objects.all()
        return render(request,"index.html",{"img":img})
    return redirect("accounts/login")'''
    return render(request,"index.html")


def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request,username=username,password=password) or auth.authenticate(request,email=username,password=password)
        if user is not None:
            time.sleep(1)
            print("Logged In successfully")
            auth.login(request,user)
            #response = render(request,"index.html")
            #return response
            return render(request,"index.html")
        else:
            mymessage = "The username or password you entered is Incorrect !"
            messages.info(request,mymessage)
            return redirect("login")
    return render(request,"MLogin.html")

@login_required(login_url="accounts/login")
def logout(request):
    '''response = redirect("accounts/login")
    request.session.flush()
    request.session.clear_expired()
    print("session deleted")
    return response'''
    auth.logout(request)
    return redirect("accounts/login")
