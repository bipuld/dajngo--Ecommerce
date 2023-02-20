from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{'title': 'welcome to django ecommerce.com'})
def contact(request):
    
    return render(request, 'contact.html',{'title': 'welcome to django ecommerce.com'})
def about(request):
    
    return render(request, 'about.html',{'title': 'welcome to django ecommerce.com'})
