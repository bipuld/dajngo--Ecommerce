from django.shortcuts import render,redirect
from django.contrib import messages
from ecommerceapp.models import Contact,Product,Order,OrderUpdate
from django.contrib import messages
from .forms import ContactForm
from math import ceil

def home(request):
    allProds = []
    catprods = Product.objects.values('category','product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params= {'allProds':allProds}
    return render(request,"home.html",params)
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


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login and Try Again")
        return redirect('login')
    new_order = None  # Define the `Order` object before the if block
    if request.method == 'POST':
        item_json = request.POST.get('itemsjson',"")
        name=request.POST.get('name','')
        amount=request.POST.get('amt')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        city=request.POST.get('city')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        new_order=Order(item_json=item_json,name=name,amount=amount,email=email,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        new_order.save()
        update=OrderUpdate(order_id=new_order.order_id,update_desc="The Order has been Placed")
        update.save()
    return render(request, 'checkout.html',{'greet':'Welcome to  Checkout page ! '})
# setup profile page in my profile that which ordr has been placed and that is pending or not
def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login and Try Again")
        return redirect('login')
    currentuser = request.user.username
    items = Order.objects.filter(email=currentuser)
    rid = None
    for i in items:
        myid = i.oid
        rid = myid.replace("Shoppify", '')
    if rid is not None:
        status = OrderUpdate.objects.filter(order_id=rid)
    else:
        status = None
    context = {
        'items': items,
        'status': status,
    }
    return render(request, 'profile.html', context)