from django.contrib import admin
from ecommerceapp.models import Contact
from django.utils.html import format_html
from .models import Product
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['sno', 'name', 'email', 'phonenumber']
    list_display_links=['name',]
    search_fields=['name', 'email', 'phonenumber']
    list_filter=['name', 'email', 'phonenumber']
    
admin.site.register(Contact,ContactAdmin)


class ProductForm(admin.ModelAdmin):
    # def thumbnail(self,object):
    #     return format_html('<img src="" style="border-radius:50px; " />'.format(object.product_photo.url))
    # thumbnail.short_description ='product_photo'
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50px; max-height:50px;" />', object.product_photo.url)
    thumbnail.short_description = 'product_photo'
    list_display=['product_id','thumbnail', 'product_name', 'category', 'subcategory','price']
    list_display_links=['thumbnail', 'product_name']
    list_filter=['product_name','category','subcategory','price']
    search_fields=['product_name','category','subcategory','price']    
    

admin.site.register(Product,ProductForm)