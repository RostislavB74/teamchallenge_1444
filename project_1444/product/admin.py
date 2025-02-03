from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
admin.site.register(Product)
admin.site.register(Category_of_jewelry)
admin.site.register(ProductImage)
admin.site.register(Categories_of_stones)
admin.site.register(Stones)
admin.site.register(Intended_to)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
# Register your models here.
