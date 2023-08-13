from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home (request): 
    special = inventory.objects.filter(special=True)
    products = inventory.objects.all()
    review = reviews.objects.all() 
    blog = blogs.objects.all()
    if(request.method == "POST"):
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
