# from django.db import models
# from django.contrib.auth.hashers import make_password,check_password
# # Create your models here.
# class Signup(models.Model):
#     email=models.EmailField()
#     pass1=models.CharField(max_length=255)
#     pass2=models.CharField(max_length=255)
    
#     def set_password(self, raw_password):
#         self.pass1=make_password(raw_password)
        
#     def check_password(self,raw_password):
#         return check_password(raw_password,self.pass1)
    
#     # def __str__(self) :
#     #     return self.email