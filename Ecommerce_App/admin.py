from django.contrib import admin
from django.shortcuts import render


# Register your models here.

from .models import Category, Product, ProductImage

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)