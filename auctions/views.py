from asyncio.windows_events import NULL
from sys import flags
from turtle import title
from unicodedata import category, name
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from numpy import flatiter

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
        d = request.POST.get("desc", None)
        p = request.POST.get("startprice", None)
        c = request.POST.get("categories", None)
        
        # Prevents user from trying to create an empty list
        if  u is None or n is None or c is None:
            return render(request, "auctions/index.html", {
                "error": "List creation failed. Missing information on created list."
            })
        else: 
            prod = List(user=u, title=n, image=i, price=p, description=d, category=c)
            prod.save()
            return HttpResponseRedirect(reverse("index"))

def about_product(request):
    if request.method == "POST":
        name = request.POST["itemname"]
        userid = request.POST["userid"]
        itemid = request.POST["itemid"]
        info = List.objects.filter(title=name)

        # To check if the user is checking their own list so they can close the auction.
        lister = False
        find_owner = User.objects.get(id=userid)
        itemowner = List.objects.get(id=itemid)
        if find_owner.username == itemowner.user:
            lister = True

        # To check for comments made on the specific list
        comments = Comments.objects.filter(commented_item_id=itemid)

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
            if lister == True:
                return render(request, "auctions/product.html", {
                    "info": info,
                    "comments": comments,
                    "watchlisted": "watchlisted",
                    "lister": "lister"
                })
            else:
                return render(request, "auctions/product.html", {
                    "info": info,
                    "comments": comments,
                    "watchlisted": "watchlisted"
                })
        else:
            if lister == True:
                return render(request, "auctions/product.html", {
                    "info": info,
                    "comments": comments,
                    "notwatchlisted": "notwatchlisted",
                    "lister": "lister"
                })
            else:
                return render(request, "auctions/product.html", {
                    "info": info,
                    "comments": comments,
                    "notwatchlisted": "notwatchlisted",
                })

def watchlist(request):
    if request.method == "POST":
        uID = request.POST["userID"]
        iID = request.POST["itemID"]
        
        items = Watchlist(item_id=iID, user_id=uID)
        items.save()

        return HttpResponseRedirect(reverse("index"))

def remove(request):
    itemid = request.POST["itemID"]
    userid = request.POST["userID"]

    # To ensure that the item is in the watchlist of the specific user. Similar to check_wl function.
    to_delete = False
    user = User.objects.filter(id=userid).values_list("id", flat=True)
    present = Watchlist.objects.filter(user_id=user[0]).values_list("item_id", flat=True)

    ids = []
    for i in present:
        ids += [i]
    for j in ids:
        if int(itemid) == j:
            to_delete = True
    
    if to_delete == True:
        deleted = Watchlist.objects.filter(item_id=itemid)
        deleted.delete()

    return HttpResponseRedirect(reverse("index"))

def check_wl(request, userN):
    user = User.objects.filter(username=userN).values_list("id", flat=True)
    user_list = Watchlist.objects.filter(user_id=user[0]).values_list("item_id", flat=True)

    # To easily get all of the lists that a user watchlisted securely
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
    if request.method == "POST":
        itemid = request.POST["itemid"]

        the_item = List.objects.filter(id=itemid)
        return render(request, "auctions/bidding.html", {
            "iteminfo": the_item
        })

def validatebid(request):
    if request.method == "POST":
        user = request.POST["username"]
        itemid = request.POST["itemid"]
        bidded = request.POST["newbid"]

        # To make sure the bid placed is higher than the current bid
        i = List.objects.filter(id=itemid).values_list("price", flat=True)
        if i[0] >= Decimal(bidded):
            return render(request, "auctions/bidding.html", {
                "errormsg": "Error. Bid placed is lesser than the current bid."
            })
        else:
            bidder = User.objects.filter(username=user).values_list("id", flat=True)
            item =  List.objects.filter(id=itemid).values_list("id", flat=True)
            newprice = Decimal(bidded)
            bid = Bids(bidder_id=bidder[0], item_id=item[0], biddedprice=newprice)
            bid.save()

            thebid = List.objects.get(id=itemid)
            thebid.price = Decimal(bidded)
            thebid.save()

            return HttpResponseRedirect(reverse("index"))

def close(request):
    if request.method == "POST":
        itemid = request.POST["itemID"]
        item_info = List.objects.get(id=itemid)
        bidder_info = Bids.objects.filter(biddedprice=item_info.price).values_list("bidder_id", flat=True)
        
        user = User.objects.filter(id=bidder_info[0]).values_list("username", flat=True)

        saved = ListDump(lister=item_info.user, winner=user[0], prodtitle=item_info.title, image=item_info.image, price=item_info.price, category=item_info.category)
        saved.save()

        deleted = List.objects.filter(id=itemid)
        deleted.delete()

        return HttpResponseRedirect(reverse("index"))

def won(request, winner):
    user = User.objects.filter(username=winner).values_list("username", flat=True)
    auctions_won = ListDump.objects.filter(winner=user[0]).values_list("id", flat=True)

    won = []
    for i in auctions_won:
        won += [i]

    items_won = ListDump.objects.filter(id__in=won)

    if won != []:
        return render(request, "auctions/won.html", {
            "items_won": items_won
        })
    else:
        return render(request, "auctions/won.html", {
            "no_wins": "It seems that you have not won any auctions yet."
        })

def categ(request):
    return render(request, "auctions/categs.html")

def view_categ(request, categ):
    category = List.objects.filter(category=categ)

    if category.exists():
        return render(request, "auctions/by_category.html", {
            "categ": category
        })
    else:
        return render(request, "auctions/by_category.html", {
            "empty_cat": "Sorry, but currently there are no lists that are under this category."
        })

def post_com(request):
    if request.method == "POST":
        com = request.POST["comment"]
        commenter_name = request.POST["commenter_name"]
        itemID = request.POST["itemID"]

        comment = Comments(comment=com, commenter=commenter_name, commented_item_id=itemID)
        comment.save()

        return HttpResponseRedirect(reverse("index"))