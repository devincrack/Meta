from django.shortcuts import render

# Create your views here.
def signup_phone(request):
    if request.method == "POST":
        uphone = request.POST["phone"]
        #add phone into models
        return render(request,"signup_Conf.html")
        if request.method == "POST":
            userOtp = request.POST["otp"]
            #authorize userOtp with realOtp
            reply = Profile.phone_verify(phone = uphone,otp = userOtp)
            if reply == "verified":
                return render(request,"signup_Name.html")
                if request.method == "POST":
                    name = request.POST["Name"]
                    #add name into models
                    return render(request,"signup_Birth.html")
                    if request.method == "POST":
                        date = request.POST["date"]
                        month = request.POST["month"]
                        year = request.POST["year"]
                        #add dob into models
                        return render(request,"signup_Username.html")
                        if request.method == "POST":
                            username = request.POST["username"]
                            #add username into models
                            return render(request,"home.html")
    return render(request,"M_p_Signup.html")
