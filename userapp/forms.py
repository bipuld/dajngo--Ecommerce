# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms
# import re
# class CustomSignupForm(UserCreationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter username','autofocus': True}))
#     email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))
#     password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
#     password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))                   
#     # this is for security stuff 
#     def clean(self):
#         cleaned_data=super().clean()
#         password1=cleaned_data.get('password1')
#         password2=cleaned_data.get('password2')
#        #  check if two passwords are same or not 
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('The password does not match')     
#         #check if password must be 7 characters and password must contain one specialcharacter 
#         if len(password1) < 7 or not re.search(r'^(?=.*[!@#$%^&*()_+\-=[\]{};\'\\:"|,.<>/?])', password1, re.I):
#             raise forms.ValidationError('The password must be at least 7 characters long and contain at least one special character') 
#         return cleaned_data
#     class Meta:
#             model=User
#             fields=['username', 'email','password1','password2']
#         # autofoucus  on username feild in signup page
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['username'].widget.attrs['autofocus'] =True