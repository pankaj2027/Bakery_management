from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (BakeryItem, BakeryItemDetails, Ingredients, Order,
                     OrderDetail)


class IngredientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('id','name')


class BakeryItemDetailsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = BakeryItemDetails
        fields = ('id','ingredient','quantity')
       

class BakeryItemSerializers(serializers.ModelSerializer):
    ingredient_details = BakeryItemDetailsSerializers(many=True) 

    class Meta:
        model = BakeryItem
        fields = ('id','name','cost_price','selling_price','quantity_inhand','ingredient_details')

    #adding bakery item with ingredients    
    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredient_details')
        bakery = BakeryItem(**validated_data)
        bakery.save()

        for item in ingredient_data:
            BakeryItemDetails.objects.create(bakery=bakery, **item)
        return bakery

    def update(self, instance, validated_data):
        ingredient_data = validated_data.pop('ingredient_details')
        instance.name = validated_data.get('name',instance.name)
        instance.cost_price = validated_data.get('cost_price',instance.cost_price)
        instance.selling_price = validated_data.get('selling_price',instance.selling_price)
        instance.quantity_inhand = validated_data.get('quantity_inhand',instance.quantity_inhand)
        instance.save()
        keep_ingredient_ids = []

        for item in ingredient_data:
            if "id" in item.keys():
                if BakeryItemDetails.objects.filter(id = item['id']).exists():
                    c = BakeryItemDetails.objects.get(id = item['id'])
                    c.quantity = item.get('quantity',c.quantity)
                    c.ingredient = item.get('ingredient',c.ingredient)
                    c.save()
                    keep_ingredient_ids.append(c.id)
                else:
                    continue
            else:
                c = BakeryItemDetails.objects.create(bakery=instance, **item)
                keep_ingredient_ids.append(c.id)

        for item in instance.ingredient_details:
            if item.id not in keep_ingredient_ids:
                item.delete()

        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


''' getting bakery item info for customer'''
class BakeryItemInfoSerializer(serializers.ModelSerializer):
    ingredient_details = BakeryItemDetailsSerializers(many=True) 

    class Meta:
        model = BakeryItem
        fields = ('id','name','selling_price','quantity_inhand','ingredient_details')


class OrderDetailSerialzer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ('bakery_item','quantity','amount')
        read_only_fields = ('amount',)

class OrderItemsSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerialzer(many=True)
    user = serializers.CharField(source="user.first_name",  read_only=True)
    
    class Meta:
        model = Order
        fields = ('user','Total_amount','order_date','order_detail')
        read_only_fields = ('Total_amount','order_date')

    def create(self,validate_data):
        order_detail_data = validate_data.pop('order_detail')

        # checking the required quantity is avaiable in bakery or not.
        for item in order_detail_data:
            quantity = item['quantity']
            quantity_inhand = item['bakery_item'].quantity_inhand
            if quantity_inhand  < quantity:
                raise serializers.ValidationError("Required {} quantity is not avaiable in stock. Avaiable quantity are {}".format(item['bakery_item'].name,quantity_inhand))  

        order = Order(**validate_data)
        order.save()   
        total_amount=0

        for item in order_detail_data:
            quantity = item['quantity']
            price = item['bakery_item'].selling_price
            amount = quantity*price
            total_amount += amount
            quantity_inhand = item['bakery_item'].quantity_inhand
            OrderDetail.objects.create(order=order,**item,amount=amount)
            BakeryItem.objects.filter(pk=item['bakery_item'].id).update(quantity_inhand = quantity_inhand-quantity)

        Order.objects.filter(pk=order.id).update(Total_amount=total_amount)
        return order

