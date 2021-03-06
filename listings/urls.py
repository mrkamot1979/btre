from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #handles the url /listings
    path('<int:listing_id>', views.listing, name='listing'), #example url would bre /listing/id where the id will be the listing_id parameter
    path('search', views.search, name='search') #this is for searching, url is /listings/search
]