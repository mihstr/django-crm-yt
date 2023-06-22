from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm

# Create your views here.
def home(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            messages.success(request, "You are logged in!")
            return redirect("website:home")
        else:
            messages.error(request, "Error! Please try again")
            return redirect("website:home")

    else:
        return render(request, "website/home.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect("website:home")

def register_user(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are registered!")
            
            return redirect("website:home")
        
        
    else:
        form = SignupForm()
        return render(request, "website/register.html", {
            "form": form,
        })
    
    return render(request, "website/register.html", {
        "form": form,
    })
