from turtle import title
from unicodedata import name
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    list_item = Product.objects.all()
    return render(request, "auctions/index.html", {
        "list_item": list_item
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new(request):
    return render(request, "auctions/new_list.html")

def create_list(request):
    if request.method == "POST":
        u = request.POST["user"]
        n = request.POST["itemtitle"]
        i = request.POST["image"]
        p = request.POST["startprice"]
        c = request.POST["categories"]

        prod = Product(user=u, title=n, image=i,price=p, category=c)
        prod.save()

        return HttpResponseRedirect(reverse("index"))

def about_product(request):
    name = request.GET["itemname"]
    info = Product.objects.filter(title=name)

    return render(request, "auctions/product.html", {
        "info": info 
    })

def bidding(request):
    pass