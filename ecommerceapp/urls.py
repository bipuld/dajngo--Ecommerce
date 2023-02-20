from django.urls import include,path
from ecommerceapp import views

urlpatterns=[
   path('',views.index,name='index')
]