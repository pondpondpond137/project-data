from django.shortcuts import render, redirect
from app_products.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context={"products":products})

def signin(request):
    return render(request, 'signin.html')


def products(request):
    all_products = Product.objects.all()
    return render(request, "products.html", context={"products":all_products})