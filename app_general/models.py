from django.contrib.auth.models import User
from django.db import models
from app_products.models import Product

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id}, {self.user.username}, {self.product.title}, {self.quantity}"