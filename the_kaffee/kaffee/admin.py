from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(inventory)
admin.site.register(reviews)
admin.site.register(blogs)
admin.site.register(contact)