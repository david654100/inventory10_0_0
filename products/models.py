from django.db import models

# Create your models here.
class product (models.Model):
    product_id = models.AutoField(primary_key=True)
    item_type = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    shipping_cost = models.FloatField(null=True, blank=True, default=None)
    price_bought = models.FloatField(null=True, blank=True, default=None)
    item_name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    color = models.CharField(max_length = 30)
    comments = models.TextField(null=True, blank=True, default=None)
