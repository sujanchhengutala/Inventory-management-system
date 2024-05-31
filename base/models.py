from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#==================================================================== 
                    # abstraction of User table
#==================================================================== 
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=100, default="username")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


#==================================================================== 
#==================================================================== 
class ItemsType(models.Model):
    name = models.CharField(max_length=100)
    
#==================================================================== 
#==================================================================== 

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    description = models.TextField(default='department')

#==================================================================== 
#==================================================================== 

class Item(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ItemsType, on_delete=models.SET_NULL, null=True)
    description = models.TextField(default='This is a item')
    quantity = models.IntegerField()
    department = models.ManyToManyField(Department)

#==================================================================== 
#==================================================================== 

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default="Kathmandu")
    company_name = models.CharField(max_length=100)
    contact_no = models.IntegerField(default='+977-xxx-xxx-xxx')
    
    
#==================================================================== 
#==================================================================== 

class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.TextField()

#==================================================================== 
#==================================================================== 
