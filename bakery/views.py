from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import BakeryItem, Ingredients, Order
from .serializers import (BakeryItemInfoSerializer, BakeryItemSerializers,
                          IngredientSerializers, OrderItemsSerializer,
                          UserSerializer)


# Adding IngredientDetails
class IngredientsDetails(viewsets.ModelViewSet):
    
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializers

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


# Adding BakeryItemsDetails 
class Bakeryitems(viewsets.ModelViewSet):

    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializers

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


# BakeryitemsInfo for the customer
class BakeryitemsInfo(viewsets.ViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        bakery_list = BakeryItem.objects.all()
        serializer = BakeryItemInfoSerializer(bakery_list, many=True )
        return Response(serializer.data)    


# Registration for the customer
class CustomerRegistration(viewsets.ViewSet):
   
    def create(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your registration has been completed Successfully!!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# placing order
class OrderItems(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = OrderItemsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            order_detail = Order.objects.all().last()
            serializer_data = OrderItemsSerializer(order_detail)
            res = serializer_data.data
            return Response(res, status=status.HTTP_201_CREATED ) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OrderHistory(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # display order history 
    def list(self,request):
        ingredient_list = Order.objects.filter(user=self.request.user)
        serializer = OrderItemsSerializer(ingredient_list, many=True )
        return Response(serializer.data)

