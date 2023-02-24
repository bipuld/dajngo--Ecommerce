from django.shortcuts import render,redirect
from django.contrib import messages
from ecommerceapp.models import Contact
from django.contrib import messages
from .forms import ContactForm
def home(request):
    return render(request, 'home.html',{'title': 'welcome to django ecommerce.com'})

# not using forms.py iin this view i am doing by using forms.py 
# def contact(request):
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         descri=request.POST.get('description')
#         phoneNumber=request.POST.get('phone-number')
#         obj=Contact(name=name,email=email,description=descri,phonenumber=phoneNumber)
#         obj.save()
#         messages.info(request,"Thank You for Contacting Us!")
#         return redirect('home')
#     return render(request, 'contact.html',{'title': 'welcome to django ecommerce.com'})


def contact(request):
    if request.method == "POST":
    # process form data
        print(request.POST)
        form = ContactForm(request.POST)
            
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact')
    else:
        form = ContactForm()
        print(form.data)
    return render(request, 'contact.html', {'form': form})
def about(request):
    
    return render(request, 'about.html',{'title': 'welcome to django ecommerce.com'})
