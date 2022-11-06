from random import choices
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
from numpy import product

STATE_CHOICES = (
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunchal Pradesh' , 'Arunchal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Chandigarh' , 'Chandigarh'),
    ('Chattishgarh' , 'Chattishgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu' , 'Daman and Diu'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('punjab','punjab'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana','Telangana'),
    ('West Bengal','West Bengal')
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile= models.IntegerField(null=True)
    locality = models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    zipcode= models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory",default=1)

    name = models.CharField(max_length=100)       

    def __str__(self):
        return self.name

    

class Product(models.Model):
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory , on_delete = models.CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    product_image = models.ImageField(upload_to = 'productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)

    def __str__(self):
        return str(self.id)    

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price        

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)   

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product , on_delete =models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICES, default ='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price 