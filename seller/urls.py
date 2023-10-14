from django.urls import path
from.views import *

urlpatterns = [
    path('allsellers/', all_sellers),
    path('addseller/', create_seller),
    path('rudseller/<int:phone>', rud_seller),
]
