from django.urls import path,include
from userapp import views
# app_name='userapp'
urlpatterns = [
   
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name="activate")
# this is will open a default activate page by djnaog whee we arre passing tokena dn uidb64 address
]
