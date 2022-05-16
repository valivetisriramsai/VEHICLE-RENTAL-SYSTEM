from django.db import models
from accounts import views
# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    status=models.BooleanField(default=False)

class Book(models.Model):
    name=models.CharField(max_length=100)
    pickup=models.CharField(max_length=100)
    returnl=models.CharField(max_length=100)
    pickd=models.DateField()
    returnd=models.DateField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    status1=models.BooleanField(default=False)
    
    #def get_orders_by_customer(email):
       # return Book.objects.filter(username=email)





class Payment(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.IntegerField()

class Payment1(models.Model):
    cardholdername=models.CharField(max_length=100)
    date=models.DateField()
    cvv=models.IntegerField()
    cardnumber=models.BigIntegerField()
    

