from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("",views.signup_email,name="signup_email"),
   path("send_Otp",views.send_Otp,name="send_Otp"),
   path("verify_Otp",views.verify_Otp,name="verify_Otp"),
]
