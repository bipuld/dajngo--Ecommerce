from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
# from userapp.forms import CustomSignupForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from userapp.utils import account_activation_token,AccountActivationTokenGenerator
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.views.generic import CreateView,View
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
        # if len(password) > 7 and 
          # Check that password meets the length and special character requirements
        if len(password) < 8 or not any(char in "!@#$%^&*()_+-={}[]|\:;\"<>,.?/~`" for char in password):
            messages.warning(request, 'Password must be at least 8 characters long and contain a special character')
            return render(request, 'signup.html')
        if confirm_password != password:
            messages.warning(request, 'Password does not match')
            return render(request,'signup.html')
            # return  HttpResponse('Passwords do not match')
        try:
            if User.objects.filter(username=email).exist():
                # return HttpResponse('User already exists')
                messages.warning(request, 'This email is already in use')
                return render(request,'login.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password) #this  1st email for the username 
        user.is_active=True
        user.save()
# for encoding mechanism for token that need  send to the user mail account in email and decoding that with this class
        
        # for sending purposes view rquirment
        email_subject='Activate your account'
        email_body=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user)
        })
        
        # email_message =EmailMessage(email_subject,email_body,settings.EMAIL_HOST_USER,[email])
        messages.success(request,f"Activate your account by clicking the link on your mail{email_body}")    
        return redirect('login')
    
    return render(request, 'signup.html') 

# for decoding mechanism for token taht is send to userr mail account in email and decoding that with this class
class ActivateAccountView(View):
    def GET(self, request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and account_activation_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info('Account has been activated')
            return redirect('login')
        return render(request, 'activationfail.html')
    
def login(request):
    if request.method == 'POST':
        username=request.POST['email']
        userpassword=request.POST['password1']
        myuser=authenticate(username=username,password=userpassword)
        # this is recaptcha form that you are not robiot till 
        # recaptcha_response=request.POST['g-recaptcha-response']      
        # if not recaptcha_response:
        #     messages.error(request,'Please Verify that your not a robot . ')
        #     return redirect(request,'login.html')
        # data={
        #     'secret':'',
        #     'response':recaptcha_response
        # }
        # response=request.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        # result=response.json()
        # if not result['success']:
        #     messages.error(request,'reCAPTCHA verification failed.')
        #     return redirect(request,'login.html')
        
        
        # here recaptcha final lone
        if myuser is not None:
            auth_login(request,myuser)
            messages.success(request,'Sucessfully logged in')
            return redirect('home')
        else:
            messages.warning(request,'invalid username or password')
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth_logout(request)
    messages.info(request,'Sucessfully logged out')
    return redirect('login')
    # return render(request,'logout.html')



