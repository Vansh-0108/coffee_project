from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as signin
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required()
def home (request): 
    special = inventory.objects.filter(special=True)
    products = inventory.objects.all() 
    review = reviews.objects.all() 
    blog = blogs.objects.all()
    if request.method == "POST":
        contact.objects.create(
            name = request.POST.get("name"),
            email = request.POST.get("email"),
            number = request.POST.get("number")
        )
        return render(
            request, "index.html", context={
                "special": special,
                "products": products,
                "review": review,
                "blog": blog,
                "saved": True
            } 
        )
    return render(request, "index.html", context={"special": special,
                                                  "products": products,
                                                  "review": review,
                                                  "blog": blog,
                                                  })

def signup(request):
    if request.method == "POST":
        my_user = User.objects.create_user(
            first_name = request.POST.get("name"),
            # last_name = request.POST.get("name").split(" ")[1],
            username = request.POST.get("email"),
            email = request.POST.get("email"),
            password = request.POST.get("password")
        )
        # my_user.save()
        user = authenticate(username = request.POST.get("email"), password = request.POST.get("password"))       
        signin(request, user)
        return redirect("home")
    return render(request, "signup.html")

def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username"),
        password = request.POST.get("password")
        # print(username, password)
        user = authenticate(request, email = username, password = password)
        if user is not None:
            signin(request, user)
            return redirect("home")
        else:
            return HttpResponse("<script> alert('Invalid Credentials');</script>")
    return render(request, "login.html")

def signout(request):
    logout(request)
    return redirect("login")