from django.shortcuts import render,HttpResponse,redirect
import random
import smtplib,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math
from database.models import User,Profile
from django.contrib import messages
import time
from datetime import date



# create your views here
def otp_Gen(rec):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        email_address = 'fromandriodmanager@gmail.com'
        me ='fromandriodmanager@gmail.com'
        you =rec
        email_password = 'itasqaclqlxvdzrs'
        connection.login(email_address, email_password )
        msgs = MIMEMultipart('alternative')
        msgs['Subject'] = "Your OTP for Metagram"
        msgs['From'] = me
        msgs['To'] = you
        digits = [i for i in range(0, 10)]
        otp = ""
        for i in range(8):
            index = math.floor(random.random() * 10)
            otp += str(digits[index])
        text = (f"Your OTP is : {otp}.\n Thank you for Registering Metagram")
        html = (f"""\
	<html>
	  <head></head>
	  <body>
	    <h3 style='text-align:center;'>Your <b>OTP</b> for Metagram is :<br> <button style="outline:none;margin-top:1em;border-radius:0.2em;border-width:0;text-align:center; font-size:30px;height:2em;" > <b>{otp}</b></button></h3>.<br>You OTP is valid for 10 Minutes.<br>
	    <p>Thank you for Registering Metagram.
	    </p>
	  </body>
	</html>
	""")
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msgs.attach(part1)
        msgs.attach(part2)
        connection.sendmail(from_addr=email_address, to_addrs=rec,
        msg=msgs.as_string())
        return otp



def signup_Continue_Username(request):
    if request.method == "POST":
        usernames = request.POST["username"]
        if User.objects.filter(username=usernames).exists():
            messages.info(request,"Sorry! Username is not Available")
            return redirect("signup_username")
        user = User.objects.create_user(username=usernames,password=request.session["password"],first_name=request.session["Name"],email=request.session["email"])
        uset.save()
        time.sleep(1)
        return HttpResponse("<h1>You are successfully pre-registered for Metagram.<br>This Website is under development. <br> When its ready, we will mail you.<br>Login with your id.</h1>")
    return render(request,"signup_Username.html")

def signup_Continue_Birth(request):
    if request.method == "POST":
        dob = request.POST["dob"]
        request.session["dob"] = dob
        #add dob into models
        return render(request,"signup_Username.html")
    return render(request,"signup_Birth.html")

def signup_Name(request):
    return render(request,"signup_Name.html")

def signup_Continue_Name(request):
    if request.method == "POST":
        name = request.POST["Name"]
        password = request.POST["password"]
        if len(password)<6 or password.isalnum() is False:
            messages.info(request,"Please enter 8 digit password to make your account strong!")
            return redirect("signup_Name")
        request.session["Name"] = name
        request.session["password"] = password
        #add name into models
        return render(request,"signup_Birth.html")
    return render(request,"signup_Name.html")

def signup_Conf(request):
    return render(request,"signup_Conf.html")


def verify_Otp(request):
    if request.method == "POST":
        userOtp = request.POST["conf_code"]
        memail = request.COOKIES.get("email")
        meOtp = request.session.get("otp")
        context = {"email":memail}
        if userOtp == meOtp:
            if request.COOKIES.get("email") is not None:
                return render(request,"signup_Name.html")
 #              mymsg = "Invalid Otp!"
            elif request.session.get("email") is None:
                messages.info(request,"sorry! otp expired!")
                return redirect("signup_Conf")
        elif userOtp != meOtp:
            if request.COOKIES.get("email") is None:
                messages.info(request,"sorry! otp expired!")
                return redirect("signup_Conf")
            else:
                mymsg = "Invalid Otp!"
                messages.info(request,mymsg)
                return redirect("signup_Conf")
    else:
        return render(request,"signup_Conf",context)



def signup_email(request):
    if request.method == "POST":
        uemail = request.POST["email"]
        request.session["email"] = uemail
        request.session["otp"] = otp_Gen(uemail)
        context = {"email":uemail}
        response = render(request,"signup_Conf.html",context)
        response.set_cookie("email",uemail,max_age=600)
        return response
    return render(request,"M_e_Signup.html")



