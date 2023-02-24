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