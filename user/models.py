from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=225)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
      