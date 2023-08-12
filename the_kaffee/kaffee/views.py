from django.shortcuts import render
from .models import *

# Create your views here.

def home (request): 
    special = inventory.objects.filter(special=True)
    products = inventory.objects.all()
    review = reviews.objects.all() 
    return render(request, "index.html", context={"special": special, "products": products, "review": review})
