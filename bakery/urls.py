from django.urls import include, path
from rest_framework import routers

from .views import Bakeryitems, BakeryitemsInfo, IngredientsDetails, OrderItems, CustomerRegistration,OrderHistory

router = routers.DefaultRouter()
router.register('ingredient', IngredientsDetails, basename='ingredients_details')
router.register('bakeryitem', Bakeryitems, basename='bakeryitem')
router.register('registration', CustomerRegistration, basename='registration')
router.register('menu', BakeryitemsInfo, basename='menu')
router.register('order', OrderItems, basename='order')
router.register('orderhistory', OrderHistory, basename='orderhistory')

urlpatterns = [
    path('', include(router.urls)),
]
