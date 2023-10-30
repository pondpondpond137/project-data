from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)


from django.db import models

class ListCartProduct(models.Model):
    user = models.ForeignKey('Client', on_delete=models.CASCADE)
    product = models.ForeignKey('app_products.Product', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.user.name}: {self.product.title} {self.amount}ea"

    class Meta:
        unique_together = ['user', 'product']  # Enforce uniqueness for user and product combination
