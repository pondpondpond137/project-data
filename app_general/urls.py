from django.urls import path
from app_general import views


urlpatterns = [
    path('<user_id>', views.home),
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('products/', views.products, name='products'),
    path('products/id_product=<product_id>', views.product, name='product'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/delete/<int:cart_id>', views.delete)
]