from django.contrib import admin
from ecommerceapp.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['sno', 'name', 'email', 'phonenumber']
    list_display_links=['name',]
    search_fields=['name', 'email', 'phonenumber']
    list_filter=['name', 'email', 'phonenumber']
    
admin.site.register(Contact,ContactAdmin)