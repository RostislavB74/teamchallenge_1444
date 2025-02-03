import uuid
from pathlib import Path
from PIL import Image
from django.conf import settings
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.core.exceptions import ValidationError, FieldError
from django.db import models, connection
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.db.models import ForeignKey
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# from category.models import Category, CategorySchema

def generate_sku():
    last_product = Product.objects.order_by('-id').first()
    if last_product:
        # Припустимо, що перші два символи - це префікс
        last_sku_number = int(last_product.sku[2:])
        new_sku = f"PR{last_sku_number + 1:05d}"  # Формат: PR00001, PR00002, ...
    else:
        new_sku = "PR00001"  # Початковий SKU
    return new_sku

class Product(models.Model):
    sku = models.CharField(max_length=10, unique=True, default=generate_sku, editable=False)
    article = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    type_of_jewelry = ForeignKey('Category_of_jewelry', on_delete=models.PROTECT, null=True, blank=True, related_name='category_of_jewelry')  # Optional field.CharField(max_length=100)
    intended_to = ForeignKey('Intended_to', on_delete=models.PROTECT, null=True, blank=True, related_name='gender')
    product_type = models.CharField(max_length=100,null=True, blank=True)
    subtype = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    price = models.DecimalField(max_digits=10, decimal_places=2)
    design =  models.CharField(max_length=100, null=True, blank=True)
    metal = models.CharField(max_length=50),
    carat = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Optional field
    metal_color = models.CharField(max_length=100, null=True, blank=True)
    material_color =models.CharField(max_length=100, null=True, blank=True)
    stone = ForeignKey('Stones', on_delete=models.PROTECT, null=True, blank=True, related_name='stones')
    stone_color = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    inlay = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    inlay_characteristics = models.TextField(null=True, blank=True)  # Optional field
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional field
    dimensions = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    size = models.CharField(max_length=20, null=True, blank=True)  # Optional field
    gift_reason = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    clasp_type = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    style = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    weave_type = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    material = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    coating = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    gold_plating = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    collection = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    set = models.BooleanField(default=False)  # Use BooleanField for 'Set'
    country_of_origin = models.CharField(max_length=50, null=True, blank=True)
    brand_name = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    image = models.ImageField(upload_to='products/', null=True, blank=True) # Add related_name
    ean_13 = models.CharField(max_length=13, null=True, blank=True)  # Optional field for EAN-13
    qr_code = models.CharField(max_length=100, null=True, blank=True)  # Optional field
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    time_update = models.DateTimeField(auto_now=False, null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return f"{self.sku} - {self.product_type}"
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

class Category_of_jewelry(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
     verbose_name_plural = "Category of jewelry" 
    def __str__(self):
        return self.name
class Types_of_stones(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Type of stones" 
    def __str__(self):
        return self.name

class Stones_base(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Stones base" 
    def __str__(self):
        return self.name
class Categories_of_stones(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
     verbose_name_plural = "Category of stones" 

    def __str__(self):
        return self.name

class Categories_of_metal(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
     verbose_name_plural = "Category of metal" 

    def __str__(self):
        return self.name

class Categories_of_materials(models.Model):
    name = models.CharField(max_length=100) 
    class Meta:
     verbose_name_plural = "Category of materials" 

    def __str__(self):  
        return self.name

class Stones(models.Model):
    name = models.CharField(max_length=100)
    type_of_stone = models.ForeignKey(Types_of_stones, on_delete=models.PROTECT, related_name='type_of_stones', null=True, blank=True)
    base_of_stone = models.ForeignKey(Stones_base, on_delete=models.PROTECT, related_name='base_of_stones', null=True, blank=True)
    category = models.ForeignKey(Categories_of_stones, on_delete=models.PROTECT, related_name='categories_of_stones',   null=True, blank=True)

    class Meta:
     verbose_name_plural = "Stones" 

    def __str__(self):
        return self.name
class Intended_to(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Intended to" 

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name
