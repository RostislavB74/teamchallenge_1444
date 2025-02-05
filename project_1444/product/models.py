from django.db import models
from treebeard.mp_tree import MP_Node
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from  model_utils.models import TimeStampedModel
# # from .utils import generate_sku

# from treebeard.mp_tree import MP_Node


# class Category(MP_Node):
#     name = models.CharField(max_length=100)
#     parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children') 
#     class Meta:
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return self.name
def generate_sku():
    last_product = Product.objects.order_by('-id').first()
    if last_product:
        # Припустимо, що перші два символи - це префікс
        last_sku_number = int(last_product.sku[2:])
        new_sku = f"PR{last_sku_number + 1:05d}"  # Формат: PR00001, PR00002, ...
    else:
        new_sku = "PR00001"  # Початковий SKU
    return new_sku

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     sku = models.CharField(max_length=10, unique=True, default=generate_sku, editable=False)
#     article = models.CharField(max_length=50, null=True, blank=True)  # Optional field
#     name = models.CharField(max_length=100, null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     jewerly_type = models.ForeignKey('JewelryCategory', on_delete=models.PROTECT, null=True, blank=True, related_name='category_of_jewelry')
#     product_type = models.CharField(max_length=100, null=True, blank=True)
#     properties = GenericRelation('Property')
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
#     class Meta:
#         verbose_name_plural = "Products"
#     def __str__(self):
#         return self.name


# class Property(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     value = models.CharField(max_length=255)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#     class Meta:
#         verbose_name_plural = "Properties"
#     def __str__(self):
#         return self.name

# class JewelryCategory(models.Model):
#     name = models.CharField(max_length=100,unique=True, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
# class JewelryProduct(Product):
#     category_product = models.ForeignKey(JewelryCategory, on_delete=models.CASCADE)
#     class Meta:
#         verbose_name_plural = "Jewelry categories"
#     def __str__(self):
#         return self.name
# class BraceletCategory(models.Model):
#     name = models.CharField(max_length=100, unique=True, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)

#     class Meta:
#         verbose_name_plural = "Bracelet categories"
#     def __str__(self):
#         return self.name
# class KeychainsCategory(models.Model):
#     name = models.CharField(max_length=100, unique=True, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)

#     class Meta:
#         verbose_name_plural = "Keychains categories"
#     def __str__(self):
#         return self.name


class Category(MP_Node):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='children')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True) 
    sku = models.CharField(max_length=10, unique=True, default=generate_sku, editable=False) 
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    properties = GenericRelation('Property')
    created_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name