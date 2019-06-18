from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class transaction (models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item_sold = models.OneToOneField()