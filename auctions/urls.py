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
    path("new_bid", views.bidding, name="bid"),
]
