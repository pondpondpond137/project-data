from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from app_users.forms import RegisterForm
from django.contrib.auth import login

# Create your views here.
def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "home.html")
        else:
            form = RegisterForm()
            context = {'form': form}
            return render(request, "app_users/register.html", context)
    else:
    # GET
        form = RegisterForm()
        context = {'form': form}
        return render(request, "app_users/register.html", context)
    
def contact(request: HttpRequest):
    return render(request, "app_users/contact.html")