from ctypes.wintypes import MSG
from email import message
from turtle import home
from django.shortcuts import render
from numpy import product
from requests import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import  query
from .models import material

# Create your views here.
def home(request):
    return render(request,"home.html")


def aboutus(request):
    return render(request,"AboutUs.html")


def faq(request):
    if request.method == "POST":
        email=request.POST['email']
        message=request.POST['message']
        myuser=query(Msg=message,email=email)
        myuser.save()
    return render(request,"faq.html")
		
		
  
#  return render(request,"faq.html")
        

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/home")


def laptop(request):
    
    products1 = material.objects.filter(category='l')
    print(products1)
    context = {"products1":products1}
    return render(request,"laptop.html",context)

def console(request):
    
    products2 = material.objects.filter(category='c')
    print(products2,"this is product 2")
    context = {"products2":products2}
    return render(request,"console.html",context)

def desktop(request):
    
    products3 = material.objects.filter(category='d')
    print(products3,"this is product 3")
    context = {"products3":products3}
    return render(request,"desktop.html",context)





def InnerProduct(request,id):
    var = material.objects.all()
    print(var)
    context = {"var":var[id-1]}
    return render(request,"InnerProduct.html",context)
    
    
    
    

