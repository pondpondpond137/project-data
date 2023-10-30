from django.shortcuts import render, redirect
from django.http import HttpRequest
from app_products.models import Product
from app_general.models import Client
from django.contrib import messages


# Create your views here.
def home(request, user_id = None):
    if user_id:
        products = Product.objects.all()
        username = Client.objects.get(id=user_id)
        return render(request, 'home.html', context={"products":products, 'username':username})
    else:
        products = Product.objects.all()
        return render(request, 'home.html', context={'products':products})

def signin(request):
    if request.method == "POST":
        print(request.POST)
        return redirect('/')

    else:
        return render(request, 'signin.html')

def products(request, user_id = None):
    if user_id:
        username = Client.objects.get(id=user_id)
        if len(request.GET) > 0:
            name_search = request.GET["search_bar"]
            do_search = []
            for name in [product.title for product in Product.objects.all()]:
                if name_search in name.lower():
                    do_search.append(name)
            if len(do_search) > 0:
                all_products = Product.objects.filter(title__in = do_search)
            else:
                messages.warning(request, "ไม่พบรายการสินค้าที่คุณค้นหา")
                all_products = Product.objects.all()
        else:
            all_products = Product.objects.all()
        # all_products = Product.objects.all()
        return render(request, "products.html", context={"products":all_products, 'username':username.name})
    else:
        if len(request.GET) > 0:
            name_search = request.GET["search_bar"]
            do_search = []
            for name in [product.title for product in Product.objects.all()]:
                print(name, name_search)
                if name_search in name.lower():
                    do_search.append(name)
            if len(do_search) > 0:
                all_products = Product.objects.filter(title__in = do_search)
            else:
                messages.warning(request, "ไม่พบรายการสินค้าที่คุณค้นหา")
                all_products = Product.objects.all()
        else:
            all_products = Product.objects.all()
        # all_products = Product.objects.all()
        return render(request, "products.html", context={"products":all_products})

def cart(request):
    return render(request, "cart.html")


def product(request: HttpRequest, product_id):
    if request.user.is_authenticated():
        pass
    print(product_id, type(product_id))
    product = Product.objects.get(id = product_id)
    return render(request, "product.html", context={"product":product})