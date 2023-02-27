from django.shortcuts import render,redirect
from django.contrib import messages
from ecommerceapp.models import Contact,Product
from django.contrib import messages
from .forms import ContactForm
from math import ceil
def home(request):
    # for displaying the product that was created in admin page in displaying in homepage   
    all_products=[]
    category_products=Product.objects.values('category','product_id')
    categ={item['category'] for item in category_products}
    for cat in categ:
        products=Product.objects.filter(category=cat)
        n=len(products)
        nslides=n // 4 + ceil((n/4) -(n//4))
        all_products.append([products,range(1,nslides),nslides])
        data={
            'all_products':all_products
        }
    return render(request, 'home.html',data)
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
