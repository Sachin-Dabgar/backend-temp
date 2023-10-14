from django.urls import path
from .views import *

urlpatterns = [
    path('todaydeal/', today_deal),
    path('todayoffer/', offers),
    path('featured/',featured_data),
    # path('todaydealcat/<str:cat_id>',today_deal_cat)

]
