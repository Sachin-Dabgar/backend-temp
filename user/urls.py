from django.urls import path
from .views import *

urlpatterns = [
    path('alluser/',all_user),
    path('adduser/',create_user),
    path('ruduser/',rud_user),
    path('login/',login)
]