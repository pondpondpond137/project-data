from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    amount = models.IntegerField()
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=50, null=True)