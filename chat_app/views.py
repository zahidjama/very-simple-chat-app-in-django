from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm#, CustomUserAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
# Create your view here.

@login_required(login_url="login")
def logoutFunc(request):
    logout(request)
    return redirect("")


def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    form=CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "signin.html", {'form': form})

@login_required(login_url="login")
def chat(request):
    if request.method=='POST':
        msg=request.POST.get("msg")
        obj=Message()
        obj.msg=msg
        obj.sender=request.user
        obj.save()

    messages=Message.objects.all().order_by("-date")
    usr=request.user
    return render(request, "chat.html", {'messages':messages, 'usr':usr})


@login_required(login_url="login")
def home_page(request):
    return render(request, "home.html")



def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=AuthenticationForm(request.POST or None)
    if request.method=='POST':
        uemail=request.POST.get("username")
        upass=request.POST.get("password")
        user=authenticate(request, email=uemail, password=upass)
        print(uemail, upass, user)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "login.html", {'form':form})