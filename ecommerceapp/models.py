from django.db import models
from datetime import  datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Contact(models.Model):
   sno=models.AutoField(primary_key=True)
   name=models.CharField(max_length=150)
   email=models.EmailField(max_length=254)
   description=RichTextField()
   phonenumber=models.BigIntegerField()
   created_at=models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
      return self.name + "-" + str(self.created_at)
   
   
# for product models storing data about product 


class Product(models.Model):
   product_id=models.AutoField(primary_key=True)
   product_name=models.CharField(max_length=200)
   category=models.CharField(max_length=200,default="")
   subcategory=models.CharField(max_length=200,default="")
   price=models.IntegerField(default=0)
   desc=RichTextField()
   product_photo=models.ImageField(upload_to="product_images") #this is product images feild which is storing ths peoduct in to the media forle making images forlder in it 
   created_at=models.DateTimeField(auto_now_add=True,blank=True)
   
   def __str__(self):
      return self.product_name
# for order purposes only and update order
class Order(models.Model):
   order_id = models.AutoField(primary_key=True)
   item_json = RichTextField()
   amount = models.IntegerField(default=0)
   name=models.CharField(max_length=80)
   email=models.EmailField()
   address1=models.CharField(max_length=200)
   address2=models.CharField(max_length=200)
   city=models.CharField(max_length=100)
   state=models.CharField(max_length=100)
   zip_code=models.CharField(max_length=100)
   oid=models.CharField(max_length=50,blank=True)
   amountpaid=models.CharField(max_length=500,blank=True,null=True)
   paymentstatus=models.CharField(max_length=20,blank=True)
   phone=models.CharField(max_length=100,default="")
   def __str__(self):
      return self.name
   
class OrderUpdate(models.Model):
   update_id=models.AutoField(primary_key=True)
   order_id=models.IntegerField(default="")
   update_desc=RichTextField()
   delivered=models.BooleanField(default=False)
   timestamp=models.DateTimeField(auto_now_add=True)
   
   
   def __str__(self):
      return self.update_desc[0:7] + "..."   
   
   
   
   
   