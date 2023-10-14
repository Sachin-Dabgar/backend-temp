from django.urls import path
from .views import *

urlpatterns = [
    # Brand Urls
    path('allbrand/', all_brands),
    path('addbrand/', add_brand),
    path('rudbrand/', get_brand),
    # Category Urls
    path('allcategories/', all_categories),
    path('addcategory/', add_category),
    path('rudcategory/', get_category),
    # Subcategory Urls
    path('allsubcat/', all_subcategories),
    path('addsubcat/', add_subcategory),
    path('rudsubcat/', get_subcategory),
    path('getsubcat/', getsubcat),
    # Products Urls
    path('allproducts/', all_products),
    path('addproduct/', add_product),
    path('rudproduct/', get_product),

    path('getcat/',getcatdetails),

]
