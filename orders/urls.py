from django.urls import path
from .views import *

urlpatterns = [
    path('allorders/',all_orders),
    path('add_order/',add_order),
    path('add_cart/', add_cart),
    path('allcart/', all_cart),
    path('rud_cart/',rud_cart),
    path('display_cart/',display_cart),
    path('add_wish/', add_wish),
    path('allwish/', all_wish),
    path('rd_wish/',rd_wish),
    path('display_wish/',display_wish),
]