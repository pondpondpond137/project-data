from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from app_products.models import Product
from app_general.models import Client, CartItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .main import Node


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

def products(request):
    # Create Binary Search Tree
    sort_by = request.GET.get("select-sort")
    all_purchases = [product.num_purchases for product in Product.objects.all()]
    all_products = Product.objects.all()
    bst = Node()
    bst.create(all_purchases.pop(0))
    
    while all_purchases:
        bst.insert(all_purchases.pop(0))
    
    print(sort_by)
    
    if len(request.GET) > 0:
        # 
        # 
        #           ใช้ Binary search tree
        # 
        # 
        name_search = request.GET["search_bar"]
        if sort_by == 'lowest':
            lowest_purchases = bst.min().val
            all_products = Product.objects.filter(num_purchases = lowest_purchases)
        elif sort_by == 'highest':
            highest_purchases = bst.max().val
            all_products = Product.objects.filter(num_purchases = highest_purchases)
        else:
            do_search = []
            for name in [product.title for product in Product.objects.all()]:
                if name_search.lower() in name.lower():
                    do_search.append(name)
            if len(do_search) > 0:
                all_products = Product.objects.filter(title__in = do_search)
            else:
                all_products = Product.objects.all()
                messages.warning(request, "ไม่พบรายการสินค้าที่คุณค้นหา")
    # all_products = Product.objects.all()
    
    return render(request, "products.html", context={"products":all_products})



@login_required
def view_cart(request):
    if request.method == "POST":
        items = CartItem.objects.filter(user = request.user)
        for item in items:
            item.product.num_purchases += item.quantity
            item.product.save()
            item.delete()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def delete(request, cart_id):
    cart = get_object_or_404(CartItem, id=cart_id)
    cart.product.amount += cart.quantity
    cart.product.save()
    cart.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect('products')

@login_required
def product(request: HttpRequest, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user
    item, created = CartItem.objects.get_or_create(user=user, product=product)
    if request.method == "POST":
        # กดซื้อแล้ว
        print(request.POST)
        amount = request.POST["amount"]
        amount = int(amount)
        if item.quantity == 1:
            amount -= 1
        product.amount -= int(amount) + 1
        item.quantity += int(amount)
        item.save()
        product.save()
        return redirect('cart')
    else:
        
        return render(request, "product.html", context={"product":product})