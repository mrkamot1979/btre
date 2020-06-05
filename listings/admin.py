from django.contrib import admin
#this page essentially handles he configuration for the admin pages for listings e.g. add, delete, edit Listings via the django administration
from .models import Listing #bring from listings > models

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')

admin.site.register(Listing, ListingAdmin) #this would enable the Listing entry in the Admin site