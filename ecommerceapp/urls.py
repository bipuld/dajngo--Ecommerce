from django.urls import include,path
from ecommerceapp import views

urlpatterns=[
   path('',views.home,name='home'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
]