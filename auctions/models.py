from datetime import datetime
from enum import auto
from time import timezone
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from decimal import Decimal

class User(AbstractUser):
    pass

class List(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=64, default=None)
    title = models.CharField(max_length=128, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=32, decimal_places=2, default=Decimal("0.01"))
    category = models.TextField(max_length=72, default=None)
    date = models.DateTimeField(default=timezone.localtime())

class Watchlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(List, on_delete=models.CASCADE)

class Bids(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(List, on_delete=models.CASCADE)
