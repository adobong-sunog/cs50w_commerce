from datetime import datetime
from enum import auto
from time import timezone
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=64, default=None)
    title = models.CharField(max_length=128)
    image = models.URLField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=32, decimal_places=2)
    category = models.TextField(max_length=72)
    date = models.DateTimeField(default=datetime.now())

class List(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

class Bids(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
