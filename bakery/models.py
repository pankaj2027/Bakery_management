from django.contrib.auth.models import User
from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name


class BakeryItem(models.Model):
  
    name = models.CharField(max_length=100, unique=True)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    quantity_inhand = models.IntegerField()
    

class BakeryItemDetails(models.Model):

    bakery = models.ForeignKey(BakeryItem, on_delete=models.CASCADE, related_name='ingredient_details')
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Total_amount = models.IntegerField(null=True)
    order_date = models.DateTimeField(auto_now=True)


class OrderDetail(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail')
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()






















