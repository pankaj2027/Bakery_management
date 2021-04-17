from django.contrib import admin
from .models import Ingredients,BakeryItem,BakeryItemDetails,Order,OrderDetail
# Register your models here.

@admin.register(Ingredients)
class Ingredients_admin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(BakeryItem)
class BakeryItem_admin(admin.ModelAdmin):
    list_display = ['id','name','cost_price','selling_price']

@admin.register(BakeryItemDetails)
class BakeryItemDetails_admin(admin.ModelAdmin):
    list_display = ['id','bakery','ingredient','quantity']

@admin.register(Order)
class Order_admin(admin.ModelAdmin):
    list_display = ['id','user','Total_amount','order_date']

@admin.register(OrderDetail)
class OrderDetail_admin(admin.ModelAdmin):
    list_display = ['id','order','bakery_item','quantity','amount']