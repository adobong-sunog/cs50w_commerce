from asyncio.windows_events import NULL
from turtle import title
from unicodedata import name
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    list_item = List.objects.all()
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
        u = request.POST.get("user", None)
        n = request.POST.get("itemtitle", None)
        i = request.POST.get("image", None)
        p = request.POST.get("startprice", None)
        c = request.POST.get("categories", None)
        
        # Prevents user from trying to create an empty list
        if  u is None or n is None or c is None:
            return render(request, "auctions/index.html", {
                "error": "List creation failed. Missing information on created list."
            })
        else: 
            prod = List(user=u, title=n, image=i,price=p, category=c)
            prod.save()
            return HttpResponseRedirect(reverse("index"))

def about_product(request):
    if request.method == "POST":
        name = request.POST["itemname"]
        userid = request.POST["userid"]
        itemid = request.POST["itemid"]
        info = List.objects.filter(title=name)

        # To check if user has already put the item on their watchlist.
        watched = False
        user = User.objects.filter(id=userid).values_list("id", flat=True)
        present = Watchlist.objects.filter(user_id=user[0]).values_list("item_id", flat=True)

        ids = []
        for i in present:
            ids += [i]
        for j in ids:
            if int(itemid) == j:
                watched = True

        if watched == True:
            return render(request, "auctions/product.html", {
                "info": info,
                "watchlisted": "watchlisted"
            })
        else:
            return render(request, "auctions/product.html", {
                "info": info,
                "notwatchlisted": "notwatchlisted"
            })

def watchlist(request):
    if request.method == "POST":
        uID = request.POST["userID"]
        iID = request.POST["itemID"]
        
        items = Watchlist(item_id=iID, user_id=uID)
        items.save()

        return HttpResponseRedirect(reverse("index"))

def check_wl(request, userN):
    user = User.objects.filter(username=userN).values_list("id", flat=True)
    user_list = Watchlist.objects.filter(user_id=user[0]).values_list("item_id", flat=True)

    # To easily get all of the lists that a user watchlisted
    ids = []
    for i in user_list:
        ids += [i]

    items_watched = List.objects.filter(id__in=ids)

    if ids != []:
        return render(request, "auctions/watchlist.html", {
            "watched": items_watched
        })
    else:
        return render(request, "auctions/watchlist.html", {
            "empty": "You have not put any items yet on your watchlist."
        })

def bidding(request):
    pass