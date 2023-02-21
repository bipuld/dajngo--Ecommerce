from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
# from userapp.forms import CustomSignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# this is custom from 
# def signup(request):
#     if request.method == 'POST':        
#         form=CustomSignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             if User.objects.filter(email=email).exists():
#                 # messages.error(request, 'This email is already registered. Please use a different email.')
#                 print('request,Your account has  not been created!')
#                 return redirect('signup')   
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()
#                 # messages.success(request, 'Your account has been created!')
#                 print('request,Your account has been created!')
#                 return redirect('login')
#     else:
#         form=CustomSignupForm()                       
#     return render(request,'signup.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if confirm_password != password:
            return render(request,'signup.html')
            # return  HttpResponse('Passwords do not match')
        try:
            if User.objects.filter(username=email).exist():
                # return HttpResponse('User already exists')
                return render(request,'login.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password) #this  1st email for the username 
        user.save()
    return render(request, 'signup.html') 
            






def login(request):
    return render(request,'login.html')


def logout(request):
    return redirect('login')
