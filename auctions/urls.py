from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="newlist"),
    path("created", views.create_list, name="create"),
    path("product", views.about_product, name="about"),
    path("watchlist", views.watchlist, name="list"),
    path("my_watchlist/<str:userN>", views.check_wl, name="watchlist"),
    path("categories", views.categ, name="category"),
    path("categories/<str:categ>", views.view_categ, name="checkcateg"),
    path("comment", views.post_com, name="post_comment"),
    path("removed", views.remove, name="remove"),
    path("new_bid", views.bidding, name="bid"),
    path("check_bid", views.validatebid, name="bidcheck"),
    path("closed", views.close, name="closebid"),
    path("auctions_won/<str:winner>", views.won, name="auctionsWon"),
]