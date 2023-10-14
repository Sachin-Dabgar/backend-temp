from django.db import models
from seller.models import Seller
from user.models import User
from products.models import Products
import uuid
# Create your models here.
class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    avaliable = models.CharField(editable=False, default="Na", max_length=100)
    
                
        
class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    units = models.IntegerField()
    total_price = models.FloatField(editable=False, max_length=25)
    
    
    def save(self, *args, **kwargs):
        product = Products.objects.get(pro_id = self.pro_id.pk)
        self.total_price = int(product.price) * self.units
        
        super(Cart, self).save(*args, **kwargs)
        
    def calculate_total_price(user_id):
        try:
            cart_items = Cart.objects.filter(user_id=user_id)
            total_price = sum(items.total_price for items in cart_items)
            data = [cart_items, total_price]
            return data
        except:
             return None
    

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    units = models.IntegerField()
    total_price = models.FloatField(editable=False)
    status = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        product = Products.objects.get(pro_id = self.pro_id.pk)
        self.total_price = product.price * self.units
        
        super(Order, self).save(*args, **kwargs)
    

