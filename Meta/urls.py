"""Meta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from emails import views as e_views
from phone import views as p_views
from login import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("login.urls")),
    path('accounts/signup/email',e_views.signup_email),
    path('accounts/signup/phone',p_views.signup_phone,name="signup_phone"),
    path('accounts/signup/verify_Otp',e_views.verify_Otp,name="verify_otp"),
    path('accounts/signup/signup_email',e_views.signup_email,name="signup_email"),
    path('accounts/signup/signup_Conf',e_views.signup_Conf,name="signup_Conf"),
    path('accounts/signup/signup_Name',e_views.signup_Name,name="signup_Name"),
    path('accounts/signup/signup_Continue_Name',e_views.signup_Continue_Name),
    path('accounts/signup/signup_Continue_Birth',e_views.signup_Continue_Birth),
    path('accounts/signup/signup_Continue_Username',e_views.signup_Continue_Username,name="signup_username"),
    path('',include("login.urls"))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
