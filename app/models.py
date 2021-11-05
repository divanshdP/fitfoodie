from django.db import models

class Customer(models.Model):
    
    cust_name=models.CharField(max_length=50,blank=False,null=False)
    cust_password=models.CharField(max_length=20,blank=False,null=False)
    cust_email=models.EmailField(primary_key=True,max_length=50,blank=False,null=False)
    cust_phone=models.CharField(max_length=10,blank=False,null=False)
    gender=(
        ("Male","Male"),
        ("Female","Female"),
    )
    cust_gender=models.CharField(max_length=6,choices=gender,default="Male")
    cust_address=models.TextField()

class Restaurants(models.Model):

    rest_name=models.CharField(primary_key=True,max_length=50,blank=False,null=False)
    rest_timing=models.CharField(max_length=50,blank=False,null=False)
    rest_logo=models.ImageField(upload_to='rest_logo')

class Menu(models.Model):
    item_id= models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=50,blank=False)
    item_price=models.CharField(max_length=50,blank=False)
    item_calories=models.CharField(max_length=50,blank=False)
    item_quantity=models.IntegerField(default=0,blank=False)
    item_logo=models.ImageField(upload_to='item_logo',default="Null")
    categorychoices=(
        ("Burgers","Burgers"),
        ("Drinks","Drinks"),
        ("Sweets","Sweets"),
        ("Pizzas","Pizzas"),
    )
    item_category=models.CharField(max_length=50,blank=False,choices=categorychoices)
    item_rest=models.ForeignKey(Restaurants,on_delete=models.CASCADE)
    

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_by=models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    order_total=models.IntegerField(default=0,blank=False)
    order_date=models.DateField(auto_now=True)

class orderItem(models.Model):
    orderitem_id = models.AutoField(primary_key=True)
    order_item_name=models.CharField(max_length=50,blank=False)
    order_item_price=models.CharField(max_length=50,blank=False)
    order_item_calories=models.CharField(max_length=50,blank=False)
    order_item_logo=models.ImageField(upload_to='item_logo',default="Null")
    order_item_quantity = models.IntegerField(default=0,blank=False)
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    
