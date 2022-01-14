from django.db import models

# Create your models here.

class Order(models.Model):
    orderNumber = models.CharField(max_length=200)
    customerName = models.CharField(max_length=200)
    quantity = models.IntegerField()
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
