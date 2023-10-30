from django.contrib import admin
from app_general.models import Client, CartItem

# Register your models here.
admin.site.register(Client)
admin.site.register(CartItem)