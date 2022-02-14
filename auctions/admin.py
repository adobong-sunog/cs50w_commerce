from django.contrib import admin

from .models import List, Bids, Comments

# Register your models here.
admin.site.register(List)
admin.site.register(Bids)
admin.site.register(Comments)
