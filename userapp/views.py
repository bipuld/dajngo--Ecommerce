from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from userapp.forms import CustomSignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def signup(request):
    if request.method == 'POST':        
        form=CustomSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            if User.objects.filter(email=email).exists():
                # messages.error(request, 'This email is already registered. Please use a different email.')
                print('request,Your account has  not been created!')
                return redirect('signup')   
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # messages.success(request, 'Your account has been created!')
                print('request,Your account has been created!')
                return redirect('login')
    else:
        form=CustomSignupForm()                       
    return render(request,'signup.html',{'form':form})
def login(request):
    return render(request,'login.html')


def logout(request):
    return redirect('login')



# if request.method == 'POST':
#     email = request.POST['email']
#     password = request.POST['password1']
#     confirm_password = request.POST['password2']
#     if password != confirm_password:
#         return HttpResponse('error')
#     try:
#         if User.objects.get(username == email):
#             return HttpResponse('error')
#     except Exception User.DoesNotExist:
#         pass
#     user = User.objects.create(username=email,password=password,password=pass
    