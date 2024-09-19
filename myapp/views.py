from django.shortcuts import render
from .models import *

# Create your views here.
def RegisterPage(request):
    return render(request,"app/registration.html")
def RegistarationHandler(request):
    if request.method=="post":
        #your logic for getting 
        firstName=request.POST['firstname']
        lastName=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        c_password=request.POST['c_password']
        if firstName=="" | lastName=="" | email=="" |phone=="" | password=="" | c_password=="":
            return render(request,'app/registration.html',{"msg":"All Field is Required *"})
        else:
            if  not password==c_password:
                return render (request,'app/regisration.html',{"msg","password and confirm password must be same"})
            else:
                newUser=Student.objects.create(firstName=firstName,lastName=lastName,email=email,phone=phone,password=password)
                newUser.save()
                return render(request,'app/login.html',{"msg","user login successfully"})

def loginHadler(request):
    return render(request,'app/login.html')            



