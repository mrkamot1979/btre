from django.contrib import admin
#this page essentially handles he configuration for the admin pages for listings e.g. add, delete, edit Listings via the django administration
from .models import Listing #bring from listings > models

class ListingAdmin(admin.ModelAdmin): #this class specifies which fields to show in the Admin page
    list_display = ('id', 'title', 'is_published', 'city', 'price', 'lst_date', 'realtor') #specifies which columns would show
    list_display_links = ('id', 'title') #makes the supplied column name a link
    #list_filter = ('realtor',) #makes a filter box on the screen to filter by the passed column
    list_editable = ('is_published',) #makes the is_published entry uncheck/checkable
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #specifies the fiels to execute a search
    list_per_page = 25 #for pagination purposes

admin.site.register(Listing, ListingAdmin) #this would enable the Listing entry in the Admin site
