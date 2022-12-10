from ctypes.wintypes import MSG
from email import message
from turtle import home
from django.shortcuts import render
from numpy import product
from requests import request
from django.shortcuts import  render, redirect , HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import  query
from .models import *

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
    id = id -4
    var = material.objects.all()
    print(var)
    context = {"var":var[id-1]}
    return render(request,"InnerProduct.html",context)
    
    
# def cart(request):
#     return render(request,"cart.html")
    
def cart(request):
    if request.method=="POST":
        user=request.user
        print(user,"this is the user")
        product_id=request.POST['product_id']
        print(product_id,"this is the product id")
        prod=material.objects.get(id=product_id)
        cart=Cart(user=user,product=prod)
        cart.save()
    return redirect('/showcart')

def showcart(request):
    user=request.user
    showcart=Cart.objects.filter(user=user)
    context={
        'showcart':showcart
    }

    amount=0.0
    total_amount=0.0
    tax=70.0
    
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    if cart_product:
        for p in cart_product:
            # print(p.product.price,'ye proce hain')
            print(p,'ye only p hain')
            teampamount=p.product.price
            print('teampamount',teampamount)
            amount=amount+teampamount
            print('amount =',amount)
            total_amount=amount+tax
            print('This is total amoutn',total_amount)
            context={
                'amount':amount,
                'total_amount':total_amount,
                'showcart':showcart
            }
       
    else:
        return HttpResponse("your Cart is Empty")


    
    return render(request,'cart.html',context)

