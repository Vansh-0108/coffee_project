from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class inventory(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    maxprice = models.IntegerField()
    image = models.ImageField(upload_to="item_photos")
    rating = models.FloatField()
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

class blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    date = models.DateField()
    desc = models.TextField()

class contact(models.Model):
    name= models.CharField(max_length=300, unique=True)
    email= models.EmailField()
    number = models.CharField(max_length=13)

