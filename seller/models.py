from django.db import models
import uuid
# Create your models here.


class Seller(models.Model):
    seller_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=225)
    account_no = models.IntegerField()
    ifsc_code = models.CharField(max_length=11)
    pan_card = models.CharField(max_length=10)
    aadhar_num = models.CharField(max_length=12)
    shipping_address = models.TextField()
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    rating = models.CharField(max_length=2)
