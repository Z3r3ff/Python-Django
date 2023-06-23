from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(default='', max_length=255)
    slug = models.SlugField(null=True, unique=True, blank=True)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(default='', max_length=255)
    description = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    product_img = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.title


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=255)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title
