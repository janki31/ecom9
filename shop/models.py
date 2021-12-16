from django.db import models

# Create your models here.

class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=30,default="")
    product_desc=models.TextField(default="")
    product_price=models.IntegerField(default=0)
    pub_date=models.DateField()
    product_image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    emailid=models.EmailField(max_length=40,default="")
    mobileno=models.IntegerField(default=0)
    feedback=models.TextField(default="")

    def __str__(self):
        return self.name

'''class Order(models.Model):
    oid=models.AutoField(primary_key=True)
    itemjson=models.CharField(max_length=2000)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30,default="")
    email=models.EmailField(max_length=50,default="")
    mobileno=models.DecimalField(max_digits=10,decimal_places=0)
    address=models.TextField(default="")
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    zipcode=models.IntegerField(default=0)
    total=models.IntegerField()

    def __str__(self):
        return self.firstname'''

class Order_detail(models.Model):
    oid=models.AutoField(primary_key=True)
    items=models.CharField(max_length=2000)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30,default="")
    email=models.EmailField(max_length=50,default="")
    mobileno=models.DecimalField(max_digits=10,decimal_places=0)
    address=models.TextField(default="")
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    zipcode=models.IntegerField(default=0)
    total=models.IntegerField()

    def __str__(self):
        return self.firstname



