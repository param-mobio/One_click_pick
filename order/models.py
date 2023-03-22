from django.db import models
from user.models import User
from products.models import Products

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for deleivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='user.order+')
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=10, null=True,blank=True)
    email = models.EmailField(null=True)
    address1 = models.CharField(max_length=20,null=True,blank=True)
    address2 = models.CharField(max_length=20,null=True,blank=True)
    total_price = models.DecimalField(null=True,decimal_places=2,max_digits=10)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, null=True,blank=True,related_name='user.order.created_by+',on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200, null=True,related_name='user.order.updated_by+' ,blank=True,on_delete=models.SET_NULL)

class OrderItem(models.Model):
    product = models.ForeignKey(Products,null=True,on_delete=models.SET_NULL,related_name='orderitem+')
    cart = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL,related_name='order+')
    size = models.CharField(null=True,blank=True,max_length=5)
    colour = models.CharField(null=True,blank=True,max_length=20)
    quantity = models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, null=True,blank=True,related_name='user.orderitem.created_by+',on_delete=models.SET_NULL)
    update_by=models.ForeignKey(User,max_length=200, null=True,related_name='user.orderitem.updated_by+' ,blank=True,on_delete=models.SET_NULL)

