from django.db import models    #type:ignore

class Contact(models.Model):
    name = models.CharField(max_length=255)  # Use CharField instead of TextField for limited text
    email = models.EmailField()
    desc = models.TextField()  # Removed max_length as it’s invalid for TextField

    def __str__(self):
        return f'{self.name} -- {self.desc[:20]}'


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images",default="")

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    id=models.AutoField(primary_key=True)
    json=models.CharField(max_length=10000)
    pp_Amount=models.IntegerField(default=0)
    pp_CustomerName=models.CharField(max_length=200)
    pp_CustomerEmail=models.CharField(max_length=300)
    pp_CustomerAddress=models.CharField(max_length=200)
    pp_CustomerCity=models.CharField(max_length=300)
    pp_CustomerZip=models.CharField(max_length=300)
    oid=models.CharField(max_length=300,blank=True)
    amountpaid=models.CharField(max_length=300,blank=True,null=True)
    amountstatus=models.CharField(max_length=300,default='')
    def __str__(self) :
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_dec=models.CharField(max_length=10000)
    delivery=models.BooleanField(default=False)
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.dec[0:20]+"......."