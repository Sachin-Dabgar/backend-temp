from django.db import models
from django.contrib.postgres.fields import ArrayField
from seller.models import Seller
import uuid


class Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    brand_name = models.CharField(max_length=255, unique=True)
    image_data = models.TextField()


class Category(models.Model):
    cat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    cat_name = models.CharField(max_length=255, unique=True)
    image_data = models.TextField()


class Subcategory(models.Model):
    sub_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    sub_name = models.CharField(max_length=255, unique=True)
    image_data = models.TextField()


class Products(models.Model):
    pro_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image_data = ArrayField(models.CharField())
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    variant = models.CharField(max_length=255)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.CharField(max_length=10)
    discount_offers = models.CharField(max_length=5)
    product_code = models.CharField(max_length=225)
    listed_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    availability = models.CharField(max_length=10)

    
