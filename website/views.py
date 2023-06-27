from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):

    records = Record.objects.all()
    
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
        return render(request, "website/home.html", {
            "records": records,
        })

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

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)    

        return render(request, "website/record.html", {
            "customer_record": customer_record,
        })
    
    else:
        messages.success(request, "You must be logged in to see that page...")
        return redirect("website:home")
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect("website:home")
    else:
        messages.success(request, "You need to login to do this.")
        return redirect("website:home")
    
def add_record(request):

    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added.")
                return redirect("website:home")
            
        return render(request, "website/add_record.html", {
            "form": form,
        })
    
    else:
        messages.success(request, "You need to be logged in to add record")
        return redirect("website:home")
