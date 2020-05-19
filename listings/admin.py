from django.contrib import admin
#this page essentially handles he configuration for the admin pages for listings e.g. add, delete, edit Listings via the django administration
from .models import Listing #bring from listings > models

admin.site.register(Listing) #this would enable the Listing entry in the Admin site